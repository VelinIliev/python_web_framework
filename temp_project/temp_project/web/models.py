from django.db import models

from temp_project.web.validators import egn_validator


class TestProfile(models.Model):
    firs_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    age = models.PositiveIntegerField()
    egn = models.CharField(
        max_length=10,
        validators=[egn_validator, ],
    )
