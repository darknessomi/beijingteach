from django.db import models


class Snippet(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=False, editable=False)
    updated = models.DateTimeField(auto_now=False, editable=False)


class Img(models.Model):
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=False, editable=False)
    updated = models.DateTimeField(auto_now=False, editable=False)
