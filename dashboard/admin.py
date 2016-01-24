from django.contrib import admin
from .models import Snippet, Page, Img, SnippetPos, ImgPos, SiteSetting

admin.site.register(Snippet)
admin.site.register(Page)
admin.site.register(Img)
admin.site.register(SnippetPos)
admin.site.register(ImgPos)
admin.site.register(SiteSetting)
