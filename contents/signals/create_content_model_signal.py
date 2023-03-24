from django.dispatch import receiver
from contents.models import Content
from django.db.models.signals import post_save
from contents.utils import SendEmail


@receiver(post_save, sender=Content)
def create_content_signal(sender, instance, created, **kwargs):
    if created:
        se = SendEmail(
            signal="pending",
            subject="Content is waiting to be reviewed",
            msg=f"Your content with id: {instance.id} is waiting to be reviewed. Have patience",
            to=instance.user.email
        ).send_email()

        print("send email signal status: ", se)

