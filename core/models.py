from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='upload')

    create_date = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )
    update_date = models.DateTimeField(
        auto_now=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='posts',
    )

    class Meta:
        ordering = ['-create_date']
