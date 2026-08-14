from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet

from .models import Article, Scope, Tag

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):


            super().clean()

            main_tags = 0  # Количество основных тегов
            total_tags = 0  # Общее количество тегов

            for form in self.forms:
                # Пропускаем пустые формы
                if not form.cleaned_data:
                    continue

                # Пропускаем формы, помеченные на удаление
                if form.cleaned_data.get('DELETE', False):
                    continue

                # Проверяем, выбран ли тег
                tag = form.cleaned_data.get('tag')
                if not tag:
                    # Если тег не выбран, пропускаем
                    continue

                total_tags += 1
                # Проверяем, является ли этот тег основным
                if form.cleaned_data.get('is_main', False):
                    main_tags += 1

                # Логика проверки
            if total_tags == 0:
                # Нет ни одного тега
                raise ValidationError('У статьи должен быть хотя бы один тег!')

            if main_tags == 0:
                # Нет основного тега
                raise ValidationError('Выберите основной тег! Отметьте один из тегов как основной.')

            if main_tags > 1:
                # Больше одного основного тега
                raise ValidationError('У статьи может быть только один основной тег!')
            return None
class ScopeInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    fields = ['tag', 'is_main']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ['title']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
