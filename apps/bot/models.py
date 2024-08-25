from django.db import models

from apps.kbs.models import Keyboard

class Trigger(models.Model):
    TYPES = [
        ('text', 'Текст'),
        ('cmd', 'Команда'),
        ('prev', 'Предыдущее сообщение'),
        ('custom', 'особый')
    ]
    caption = models.CharField(verbose_name="Наименование", max_length=50, default='Сообщение', unique=True)
    type = models.CharField(verbose_name="", max_length=30, choices=TYPES, default='text')
    value = models.CharField(verbose_name="Значение", max_length=150, default="текст")

    class Meta:
        verbose_name = 'Тригер'
        verbose_name_plural = 'Тригеры'

    def __str__(self):
        return self.caption

class UserStatus(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=50, default='Статус', unique=True)

    class Meta:
        verbose_name = 'Статус пользователя'
        verbose_name_plural = 'Статусы пользователей'

    def __str__(self):
        return self.caption

class State(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=50, default='Состояние', unique=True)

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'

    def __str__(self):
        return self.caption

class StaticMessages(models.Model):
    caption = models.CharField(verbose_name="Наименование*", max_length=50, default='Сообщение', unique=True)
    text = models.TextField(verbose_name="Текст сообщения", null=True, blank=True)
    keyboard = models.ForeignKey(Keyboard, verbose_name="Клавиатура", on_delete=models.SET_NULL, null=True, blank=True)
    delay = models.IntegerField(verbose_name='Задержка перед отправкой*', default=0)
    state = models.ForeignKey(State, verbose_name='Состояние*', on_delete=models.SET_NULL, null=True)
    user_status = models.ForeignKey(UserStatus, verbose_name='Статус*', on_delete=models.SET_NULL, null=True)
    trigger = models.ForeignKey(Trigger, verbose_name='Тригер', on_delete=models.SET_NULL, null=True, blank=True)
    auto_next = models.ForeignKey('self', verbose_name="Автопереход к сообщению", null=True, blank=True, on_delete=models.SET_NULL)
    new_state = models.ForeignKey(State, verbose_name="Новое состояние", related_name="new_state", on_delete=models.SET_NULL, null=True, blank=True)
    new_status = models.ForeignKey(UserStatus, verbose_name="Новый статус", related_name="new_status", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.caption
