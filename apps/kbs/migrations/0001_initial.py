# Generated by Django 5.1 on 2024-08-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(default='Button000', max_length=50, unique=True, verbose_name='Индификатор')),
                ('text', models.CharField(default='TextButton', max_length=75, verbose_name='Текст на кнопке')),
                ('callback', models.CharField(blank=True, max_length=50, null=True, verbose_name='CallBack от кнопки (инлайн клавиатура)')),
                ('row', models.IntegerField(default=0, verbose_name='Строка')),
                ('range', models.IntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Кнопка',
                'verbose_name_plural': 'Кнопки',
            },
        ),
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(default='Button000', max_length=50, unique=True, verbose_name='Индификатор')),
                ('type', models.CharField(choices=[('std', 'Стандартная'), ('inl', 'Inline')], default='std', max_length=3, verbose_name='Тип клавиатуры')),
                ('buttons', models.ManyToManyField(to='kbs.button', verbose_name='Кнопки')),
            ],
            options={
                'verbose_name': 'Клавиатура',
                'verbose_name_plural': 'Клавиатуры',
            },
        ),
    ]
