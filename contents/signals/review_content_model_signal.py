from django.dispatch import receiver
from contents.models import Content
from django.db.models.signals import post_save
from contents.utils import SendEmail


@receiver(post_save, sender=Content)
def review_content_signal(sender, instance, **kwargs):
    if instance.review_notes:
        se = SendEmail(
            signal=f"{instance.status}",
            subject=f"Content is {instance.review_notes}",
            msg=f"Your content with id: {instance.id} is {instance.review_notes.lower()}",
            to=instance.user.email
        ).send_email()

        print("send email signal status: ", se)

