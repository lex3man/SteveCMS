from django.db import models

class StaticMessages(models.Model):
    caption = models.CharField(verbose_name="Наименование", max_length=50, default='Сообщение', unique=True)
    text = models.TextField(verbose_name="Текст сообщения")

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

