from django.db import models
from django.core.mail import send_mail


class Visitor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_valid = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    def send_mail(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Message(models.Model):
    subject = models.CharField(max_length=140)
    content = models.TextField()
    visitor = models.ForeignKey(Visitor, related_name="messages", null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
