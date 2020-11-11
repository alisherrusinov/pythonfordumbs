from django.db import models


class LessonModel(models.Model):
    slug = models.SlugField(unique=True, verbose_name='Слаг страницы')
    embed_url = models.TextField(unique=True, verbose_name='Ссылка на видео')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    script = models.TextField(verbose_name='Скрипт урока')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class AttachedLinkModel(models.Model):
    label = models.CharField(verbose_name='Подпись', max_length=300, default='Полезная ссылка')
    link = models.TextField(verbose_name='Ссылка')
    attached_to = models.ForeignKey(LessonModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.attached_to}: {self.label}'


class TimeCodeModel(models.Model):
    label = models.CharField(verbose_name='Подпись', max_length=200, default='Таймкод')
    start = models.CharField(verbose_name='Старт', max_length=5)
    finish = models.CharField(verbose_name='Конец', max_length=5)
    attached_to = models.ForeignKey(LessonModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.attached_to}: {self.label}'


class CurrentLesson(models.Model):
    username = models.CharField(max_length=100)
    attached_to = models.ForeignKey(LessonModel, on_delete=models.CASCADE)
