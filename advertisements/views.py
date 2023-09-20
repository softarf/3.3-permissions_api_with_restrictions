from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    # Разрешения на уровне представления (контроллера).
    permission_classes = []    # Добавляются права возвращаемые get_permissions() # IsAdmin
    filter_backends = [DjangoFilterBackend, SearchFilter]

    filterset_class = AdvertisementFilter
    #     Точное совпадение по полям. Задаётся внутри класса (Meta.fields=).
    #     filterset_fields = ['creator', 'title', 'description', 'created_at']

    def get_permissions(self):
        """ Выдаёт права на действия.
            Действия (action): 'create', 'update', 'partial_update', 'destroy', 'list',  'retrieve'  и 'favourite'.
            Соответствуют:      'POST',    'PUT',     'PATCH',        'DELETE', 'GET',  'GET.../id/' и 'GET.../fav/'
        """
        # "Создавать заметки можно только авторизованным пользователям."
        if self.action in ['create']:    # , 'favourite'
            return [IsAuthenticated()]

        # "Обновлять и удалять можно только свои заметки."
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwner()]

        return []    # "Просматривают все", согласно глобальной настройки.
