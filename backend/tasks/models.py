from django.db import models
from django.conf import settings
import datetime


class Task(models.Model):
    """Модель задач"""
    TASK_STATUS_CHOICES = [
        ('assigned', 'Задача принята'),
        ('review', 'Задача на ревью'),
        ('completed', 'Задача завершена'),
        ('revised', 'Есть замечания'),
    ]
    TASK_PRIORITY_CHOICES = [
        (1, 'Низкий'),
        (2, 'Средний'),
        (3, 'Высокий'),
    ]
    task_title = models.CharField(
        verbose_name='Название задачи',
        max_length=50
    )
    team_lead_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='delegated_tasks',
        verbose_name='Тимлидер'
    )
    employee_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='accepted_tasks',
        verbose_name='Исполнитель'
    )
    task_description = models.TextField(
        verbose_name='Описание задачи'
    )
    task_date_start = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата назначения задачи'
    )
    task_date_modified = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления задачи'
    )
    task_date_finish = models.DateField(
        verbose_name='Плановая дата завершения задачи'
    )
    task_status = models.CharField(
        verbose_name='Текущий статус задачи',
        choices=TASK_STATUS_CHOICES,
        max_length=20
    )
    task_priority = models.IntegerField(
        verbose_name='Приоритет задачи',
        choices=TASK_PRIORITY_CHOICES,
        default=1
    )

    @property
    def is_expired(self):
        """Проверяем, что задача не просрочена"""
        if self.task_date_finish:
            return datetime.date.today() > self.task_date_finish
        return False

    def __str__(self):
        return str(self.task_title)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
