from django.db import models
from django.conf import settings


class Content(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_written_content'
    )
    content = models.TextField(max_length=2000, null=True, blank=True)
    