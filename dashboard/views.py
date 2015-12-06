from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from home.models import Message
from .models import Snippet

def index(request):
    messages = Message.objects.order_by('-updated')
    return render(request, 'dashboard/index.html', locals())

def snippets(request):
    snippets = Snippet.objects.order_by('-updated')
    return render(request, 'dashboard/snippets.html', locals())

def new_snippet(request):
    if request.method == "POST":
        new_snippet = {}
        new_snippet['subject'] = request.POST.get('subject')
        new_snippet['content'] = request.POST.get('content', '')

        #TODO form validation
        if new_snippet['subject']:
            Snippet.objects.create(**new_snippet)

        return redirect(reverse('dashboard:snippets'))
    return render(request, 'dashboard/new_snippet.html', locals())
