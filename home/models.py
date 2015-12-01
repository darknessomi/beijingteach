from django.db import models
from dashboard.models import Snippet, Img


class Position(models.Model):
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.slug


class SnippetPos(Position):
    snippet = models.ForeignKey(Snippet, related_name="position")


class ImgPos(Position):
    img = models.ForeignKey(Img, related_name="position")


def init_all():
    pass
