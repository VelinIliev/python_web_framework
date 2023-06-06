from django.db import models


class Employee(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
    )
    seniority_level = models.CharField(
        max_length=30,
        choices=(
            ('Senior', 'Senior'),
            ('Junior', 'Junior'),
            ('Regular', 'Regular'),
        )
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
