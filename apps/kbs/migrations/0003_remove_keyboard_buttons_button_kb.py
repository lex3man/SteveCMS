# Generated by Django 5.1 on 2024-08-25 20:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbs', '0002_alter_keyboard_caption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyboard',
            name='buttons',
        ),
        migrations.AddField(
            model_name='button',
            name='kb',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kbs.keyboard', verbose_name='Клавиатура'),
        ),
    ]
