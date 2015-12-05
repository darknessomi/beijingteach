from django.shortcuts import render
from home.models import Message

def index(request):
    messages = Message.objects.all()
    return render(request, 'dashboard/index.html', locals())

def snippets(request):
    return render(request, 'dashboard/snippets.html', locals())
