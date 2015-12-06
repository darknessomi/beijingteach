from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Message, SnippetPos


def index(request):
    return render(request, 'home/index.html')


def about(request):
    snippet = SnippetPos.objects.get_snippet(slug='about')
    return render(request, 'home/about.html', locals())


def experience(request):
    snippet = SnippetPos.objects.get_snippet(slug='experience')
    return render(request, 'home/experience.html', locals())


def china(request):
    snippet = SnippetPos.objects.get_snippet(slug='china')
    return render(request, 'home/china.html', locals())


def accommodations(request):
    snippet = SnippetPos.objects.get_snippet(slug='accommodations')
    return render(request, 'home/accommodations.html', locals())


def contact(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        name = request.POST.get('name')
        email = request.POST.get('email')

        #TODO form validation
        if subject and message and name and email:
            Message.objects.new_message_from(name, email,
                                             subject=subject, content=message)

        return redirect(reverse('contact'))
    return render(request, 'home/contact.html')

def apply(request):
    return render(request, 'home/apply.html')
