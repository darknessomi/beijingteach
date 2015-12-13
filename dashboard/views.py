from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from home.models import Message
from .models import Snippet
from .forms import SnippetForm

def index(request):
    messages = Message.objects.order_by('-updated')
    return render(request, 'dashboard/index.html', locals())

def snippets(request):
    snippets = Snippet.objects.order_by('-updated')
    return render(request, 'dashboard/snippets.html', locals())

def new_snippet(request):
    form = SnippetForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse('dashboard:snippets'))
    else:
        form = SnippetForm()

    return render(request, 'dashboard/new_snippet.html', locals())
