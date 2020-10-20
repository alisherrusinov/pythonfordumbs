from django.db import models


# Create your models here.
class LessonModel(models.Model):
    slug = models.SlugField(unique=True, verbose_name='Слаг страницы')
    embed_url = models.URLField(unique=True, verbose_name='Ссылка на видео')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    script = models.TextField(verbose_name='Скрипт урока')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
