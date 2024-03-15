from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(max_length=100, verbose_name='Электронная почта')
    full_name = models.CharField(max_length=100, verbose_name='Ф.И.О.')
    comment = models.TextField(verbose_name='Комментарий')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    def __str__(self):
        return f'{self.email} {self.full_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Mailing(models.Model):
    start_time = models.DateTimeField(verbose_name='Время рассылки')
    frequency_choices = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]
    frequency = models.CharField(max_length=10, choices=frequency_choices, verbose_name="Периодичность рассылки")
    status_choices = [
        ('created', 'Created'),
        ('started', 'Started'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, verbose_name="Статус рассылки")
    recipient = models.ManyToManyField(Client, verbose_name="Получатель")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)


class Message(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')
    subject = models.CharField(max_length=100, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.subject} {self.body}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Log(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    stamp_time = models.DateTimeField(auto_now_add=True, verbose_name='Время последней рассылки')
    status = models.CharField(max_length=20, verbose_name='Статус лога')
    response = models.TextField(blank=True, verbose_name='Отклик')

    def __str__(self):
        return f'{self.message} {self.stamp_time} {self.status}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
