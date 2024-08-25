# Generated by Django 5.1 on 2024-08-22 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_state_trigger_userstatus_staticmessages_auto_next_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trigger',
            name='value',
            field=models.CharField(default='текст', max_length=150, verbose_name='Значение'),
        ),
        migrations.AlterField(
            model_name='state',
            name='caption',
            field=models.CharField(default='Состояние', max_length=50, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='userstatus',
            name='caption',
            field=models.CharField(default='Статус', max_length=50, unique=True, verbose_name='Наименование'),
        ),
    ]
