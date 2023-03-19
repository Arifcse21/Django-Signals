from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class SendEmail:

    def __init__(self, signal, subject, msg, to):
        self.subject = subject
        self.msg = msg
        self.signal = signal
        self.to = to
        self.host_user = settings.EMAIL_HOST_USER
        self.msg_html = render_to_string('email/email_template.html', {
            "signal": self.signal, "msg": self.msg, "subject": self.subject
        })
        self.msg_plain = strip_tags(self.msg_html)

    def send_email(self):

        return send_mail(
            self.subject,
            self.msg_html,
            self.host_user,
            [self.to, ],
            html_message=self.msg_html,
            fail_silently=True
        )
# SendEmail('with signal', 'custom signal msg', 'approved', 'abc@gmail.com').send_email()
