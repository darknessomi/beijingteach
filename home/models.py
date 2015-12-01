from django.db import models
from django.core.mail import send_mail
from dashboard.models import Snippet, Img


class Position(models.Model):
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.slug


class SnippetPos(Position):
    snippet = models.ForeignKey(Snippet, related_name="positions")


class ImgPos(Position):
    img = models.ForeignKey(Img, related_name="positions")


class Applicant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    is_valid = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=False, editable=False)

    def email_applicant(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Message(Snippet):
    applicant = models.ForeignKey(Applicant, related_name="messages")


def init_all():
    pass
