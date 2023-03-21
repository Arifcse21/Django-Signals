from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from contents.utils import SendEmail

STATUS = (
    ('pending', 'pending'),
    ('approved', 'approved'),
    ('deleted', 'deleted'),
    ('banned', 'banned')
)


def serial():
    last_entry = Content.objects.all().order_by("id").last()
    if last_entry:
        return last_entry.id + 1
    return 1


class Content(models.Model):
    id = models.AutoField(primary_key=True, default=serial)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_written_content'
    )
    content = models.TextField(max_length=2000, null=True, blank=True)
    status = models.CharField(choices=STATUS, default='pending')
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.id


@receiver(post_save, sender=Content)
def create_content(sender, instance, created, **kwargs):
    if created:
        se = SendEmail(
            signal="pending",
            subject="Content is waiting to be reviewed",
            msg=f"Your content with id: {instance.id} is waiting to be review. Have patience",
            to=instance.user.email
        ).send_email()

        print("send email signal status: ", se)

