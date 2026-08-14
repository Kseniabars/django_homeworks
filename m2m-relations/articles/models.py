from django.db import models




class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название тега')
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    def __str__(self):
        return self.name


class Scope(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False, verbose_name='Основной тег')

    class Meta:
        verbose_name = 'Тег статьи'
        verbose_name_plural = 'Теги статьи'

        constraints = [
            models.UniqueConstraint(
                fields=['article'],
                condition=models.Q(is_main=True),
                name='unique_main_tag_per_article'
            )
        ]



class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, related_name='articles', through='Scope', through_fields=('article' , 'tag'))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title