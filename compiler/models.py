from django.db import models


# Create your models here.
class TestModel(models.Model):
    test_input = models.TextField(verbose_name='Входные данные')
    test_output = models.TextField(verbose_name='Вывод')
    attached_to = models.ForeignKey()

    def __str__(self):
        return f'Тест для {self.attached_to}'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

