from django.contrib import admin
from .models import Snippet, Img, SnippetPos, ImgPos

admin.site.register(Snippet)
admin.site.register(Img)
admin.site.register(SnippetPos)
admin.site.register(ImgPos)
