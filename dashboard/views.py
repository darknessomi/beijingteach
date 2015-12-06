from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from home.models import Message, SnippetPos
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
        position = request.POST.get('position', '')

        #TODO form validation
        if new_snippet['subject']:
            s = Snippet.objects.create(**new_snippet)

            sp_set = SnippetPos.objects.filter(slug=position)
            if len(sp_set) == 1:
                sp_set[0].snippet = s
                sp_set[0].save()

        return redirect(reverse('dashboard:snippets'))

    snippet_pos = SnippetPos.objects.all()
    return render(request, 'dashboard/new_snippet.html', locals())
