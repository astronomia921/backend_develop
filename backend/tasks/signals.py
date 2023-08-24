from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Task


@receiver(pre_save, sender=Task)
def status_checker(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        current = instance
        previous = Task.objects.get(id=instance.id)
        if previous.task_status != current.task_status:
            return f'Статус {previous.task_status} изменен на {current.task_status}'
