from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from dashboard.models import SnippetPos
from .forms import MessageForm, ApplicantForm


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
    form = MessageForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse('contact'))

    return render(request, 'home/contact.html', locals())


def apply(request):
    form = ApplicantForm(request.POST or None)

    # need a online test
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse('apply'))

    return render(request, 'home/apply.html', locals())
