# Generated by Django 3.1.3 on 2020-11-21 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_attachedlinkmodel_label'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachedlinkmodel',
            options={'verbose_name': 'Полезная ссылка', 'verbose_name_plural': 'Полезные ссылки'},
        ),
        migrations.AlterModelOptions(
            name='timecodemodel',
            options={'verbose_name': 'Таймкод', 'verbose_name_plural': 'Таймкоды'},
        ),
        migrations.AlterField(
            model_name='attachedlinkmodel',
            name='link',
            field=models.TextField(verbose_name='Ссылка'),
        ),
    ]
