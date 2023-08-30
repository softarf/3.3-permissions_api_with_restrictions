from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Задаёт сериализатор для объявления."""

    # creator = UserSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at', )
        read_only_fields = ['creator']

    def create(self, validated_data):
        """Создаёт объявление."""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    # def validate_status(self, value):
    #     # Проверка персональным валидатором для поля 'status', почему-то не поддерживается.
    #     # Заработало случайно.
    #     # Работает с запросами 'POST', 'PUT' и 'PATCH'.
    #     # Вызывается только в том случае, если в запросе значение поля 'status' передаётся ЯВНО.
    #     """
    #         Проверяет возможность добавления нового объявления в статусе "Опубликованное/Открытое".
    #     """
    #     print("Это сработала проверка поля 'status'")
    #
    #     return value

    def validate(self, data):
        """ Проверяет полученные данные на корректность. Вызывается при создании и обновлении.

            При 'POST' вызывается перед методом 'perform_create()' (из класса
            'ModelViewSet'), если объявлен, а за тем методом 'create()'.
            При 'PUT' и 'PATCH' - после метода 'validate_status()', если объявлен, и перед методом 'update()'.
            Проверяет возможность добавления нового объявления в статусе "Опубликованное/Открытое".
        """
        opened = AdvertisementStatusChoices.OPEN
        creator = self.context['request'].user
        # status = self.context["request"].data.get("status", "")    # Можно так
        status = data.get("status", "")
        if not status and self.context['view'].action in ['create', 'update']:
            status = opened
        if status == opened and not bool(self.instance and self.instance.status == opened):
            opened_count = Advertisement.objects.filter(creator=creator, status=opened).count()
            if opened_count >= 3:
                raise ValidationError('У вас превышен лимит опубликованных объявлений (не больше 3).')
        return data

    # def update(self, instance, validated_data):
    #     """ Переопределяет метод изменяющий объект модели.
    #
    #         'instance' - "старый" объект,
    #         'validated_data' - "новые" значения полей.
    #
    #         При 'PUT' запросе обязательные поля передавать все.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.save()
    #     return super().update(instance, validated_data)
