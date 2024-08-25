from django.db import models

class Button(models.Model):
    caption = models.CharField(verbose_name="Индификатор", max_length=50, default="Button000", unique=True)
    text = models.CharField(verbose_name="Текст на кнопке", max_length=75, default="TextButton")
    callback = models.CharField(verbose_name="CallBack от кнопки (инлайн клавиатура)", max_length=50, null=True, blank=True)
    row = models.IntegerField(verbose_name="Строка", default=0)
    range = models.IntegerField(verbose_name="Порядок", default=0)

    class Meta:
        verbose_name = 'Кнопка'
        verbose_name_plural = 'Кнопки'

    def __str__(self):
        return self.caption

class Keyboard(models.Model):
    TYPES = [
        ('std', 'Стандартная'),
        ('inl', 'Inline')
    ]
    caption = models.CharField(verbose_name="Индификатор", max_length=50, default="Keyboard", unique=True)
    type = models.CharField(verbose_name="Тип клавиатуры", max_length=3, choices=TYPES, default="std")
    buttons = models.ManyToManyField(Button, verbose_name="Кнопки")

    class Meta:
        verbose_name = 'Клавиатура'
        verbose_name_plural = 'Клавиатуры'

    def __str__(self):
        return self.caption
