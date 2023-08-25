from django.contrib import admin

from advertisements.models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'creator', 'created_at', 'updated_at']
    list_display_links = ['id', 'title', 'updated_at']
    search_fields = ['id', 'title', 'creator', 'updated_at','status']
    list_filter = ('title', 'creator', 'updated_at','status')
    # Поля, которые можно редактировать прямо в админке. Не могут быть одновременно ссылками!
    list_editable = ('status', )
