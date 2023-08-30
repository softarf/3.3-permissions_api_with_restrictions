from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    # Разрешения на уровне представления (контроллера).
    permission_classes = []

    def get_permissions(self):
        """ Выдаёт права на действия.
            Действия: 'create', 'update', 'partial_update', 'destroy', 'list' и 'retrieve'.
            Соответствуют: 'POST', 'PUT',     'PATCH',      'DELETE'    'GET' и 'GET.../id/'
        """
        # "Создают только авторизованные"
        if self.action in ['create']:
            return [IsAuthenticated()]

        # "Обновляют и удаляют только авторы"
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwner()]

        return []    # "Просматривают все, (согласно глобальной настройки)"
