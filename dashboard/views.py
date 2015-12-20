from django.shortcuts import render, redirect, get_object_or_404
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

    return render(request, 'dashboard/edit_snippet.html', locals())

def update_snippet(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    initial = {}
    if snippet.has_pos():
        initial = {'position': snippet.position.slug}

    form = SnippetForm(request.POST or None, initial=initial, instance=snippet)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse('dashboard:snippets'))

    return render(request, 'dashboard/edit_snippet.html', locals())
