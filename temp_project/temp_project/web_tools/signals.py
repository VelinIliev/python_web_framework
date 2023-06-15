from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

from temp_project.web_tools.models import Employees

UserModel = get_user_model()


@receiver(signals.post_save, sender=Employees)
def handle_employee_created(*args, **kwargs):
    print(args)
    print(kwargs)


@receiver(signals.post_save, sender=UserModel)
def create_employee_on_user_created(instance, created, *args, **kwargs):
    if not created:
        return
    Employees.objects.create(
        user_id=instance.pk,
    )
