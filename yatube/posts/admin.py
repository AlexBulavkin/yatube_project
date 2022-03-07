from django.contrib import admin
# Из модуля models импортируем модели Post, Group
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk',
                    'text',
                    'pub_date',
                    'author',
                    'group',)
    # Добавляем возможность редактирования поля group
    list_editable = ('group',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)
# Регистрируем  модель Group
admin.site.register(Group)
