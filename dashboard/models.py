from django.db import models


class Snippet(models.Model):
    subject = models.CharField(max_length=140)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '{} ({})'.format(self.subject, self.updated)

    def has_pos(self):
        return len(SnippetPos.objects.filter(snippet=self)) == 1


class Img(models.Model):
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)


class Position(models.Model):
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.slug


class SnippetPosManager(models.Manager):

    def get_snippet(self, **kwargs):
        sp = self.filter(**kwargs)
        return sp[0].snippet if sp else None


class SnippetPos(Position):
    snippet = models.OneToOneField(Snippet, related_name="position", null=True, blank=True)
    objects = SnippetPosManager()

    class Meta:
        verbose_name_plural = "Snippet Positons"


class ImgPos(Position):
    img = models.ForeignKey(Img, related_name="position")

    class Meta:
        verbose_name_plural = "Img Positons"
