""" Права пользователей выдаёт метод .has_perm().
    Доступные операции: view   - просмотр;
                        add    - добавление;
                        change - изменение;
                        delete - удаление.
    Например: >>> user.has_perm("advertisements.delete_advertisement")
              False - удалять не может.

    Получить список всех доступных действий можно командой:
    Например: >>> user.get_user_permissions()
      {'advertisements.view_advertisement', 'advertisements.add_advertisement'}, только просматривать и создавать новые.
"""
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """ Класс Разрешения на подтверждение авторства."""

    def has_object_permission(self, request, view, obj):    # Разрешение на уровне объекта.
        """ Подтверждает авторство объявления.
        """
        return request.user == obj.creator
