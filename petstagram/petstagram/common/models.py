from django.contrib.auth import get_user_model
from django.db import models

from petstagram.photos.models import Photo

UserModel = get_user_model()


class Comment(models.Model):
    MAX_COMMENT_SIZE = 300

    comment_text = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_COMMENT_SIZE,
    )

    published_on = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=True
    )

    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
