from django.db import models
from django.conf import settings

STATUS = (
    ('pending', 'pending'),
    ('approved', 'approved'),
    ('deleted', 'deleted'),
    ('banned', 'banned')
)


class Content(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_written_content'
    )
    content = models.TextField(max_length=2000, null=True, blank=True)
    status = models.CharField(choices=STATUS, default='pending')

    def __repr__(self):
        return self.id
