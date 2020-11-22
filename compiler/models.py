from django.db import models
from course import models as course_models


class HomeWorkModel(models.Model):
    decs = models.TextField(default='Описание задачи')
    attached_to = models.ForeignKey(
        course_models.LessonModel,
        on_delete=models.CASCADE,
        verbose_name="Урок",
        unique=True
    )

    def __str__(self):
        return f'Дз для {self.attached_to}'

    class Meta:
        verbose_name = 'Домашка'
        verbose_name_plural = 'Домашки'


# Create your models here.
class TestModel(models.Model):
    test_input = models.TextField(verbose_name='Входные данные')
    test_output = models.TextField(verbose_name='Вывод')
    attached_to = models.ForeignKey(
        HomeWorkModel,
        on_delete=models.CASCADE,
        # default=HomeWorkModel.objects.all()[0]
    )

    def __str__(self):
        return f'Тест для {self.attached_to} номер {self.id}'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
