from django.db import models


class Snippet(models.Model):
    subject = models.CharField(max_length=140)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '{} ({})'.format(self.subject, self.updated)


class Img(models.Model):
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
