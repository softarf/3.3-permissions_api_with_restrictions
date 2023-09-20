from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    # Объявление фильтров.
    # Объявленные фильтры title и description работают корректно.
    title = filters.CharFilter(field_name="title", lookup_expr='iexact')
    description = filters.CharFilter(field_name="description", lookup_expr='icontains')

    # created_at объявленное как DateFilter корректно работает при поиске по дате.
    # Но не работает поиск интервалов created_at_after и created_at_before.
    # created_at = filters.DateFilter(field_name="created_at", lookup_expr='date')

    created_at = filters.DateFromToRangeFilter(field_name="created_at", lookup_expr='date')
    # created_at объявленное как DateFromToRangeFilter перестаёт работать при поиске по дате.
    # Но начинает работать поиск интервалов created_at_after и created_at_before.

    created_at_after = filters.DateFromToRangeFilter(field_name="created_at", lookup_expr='gte')
    created_at_before = filters.DateFromToRangeFilter(field_name="created_at", lookup_expr='lte')

    class Meta:
        model = Advertisement
        #     Базовые фильтры (сгенерированные автоматически).
        # Находят точное совпадение при поиске в указанном поле.
        fields = ['creator', 'title', 'description']
        # Объявленные через словарь ничего не находят, хотя и присутствуют в классе AdvertisementFilter.
        # fields = {
        #     'creator': ['exact'],
        #     'title': ['iexact'],
        #     'description': ['icontains'],
        # }
