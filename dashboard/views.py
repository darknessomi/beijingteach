from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from home.models import Message, Applicant
from .models import Snippet, Page, Img
from .forms import SnippetForm, PageForm, ImgForm

dashboard_login_required = login_required(login_url='/dashboard/login/')


@dashboard_login_required
def index(request):
    messages = Message.objects.order_by('-updated')
    return render(request, 'dashboard/index.html', locals())


@dashboard_login_required
def snippets(request):
    snippets = Snippet.objects.order_by('-updated')
    return render(request, 'dashboard/snippets.html', locals())


@dashboard_login_required
def pages(request):
    pages = Page.objects.order_by('-updated')
    return render(request, 'dashboard/pages.html', locals())


@dashboard_login_required
def images(request):
    images = Img.objects.order_by('-updated')
    return render(request, 'dashboard/images.html', locals())


@dashboard_login_required
def applicants(request):
    applicants = Applicant.objects.order_by('-updated')
    return render(request, 'dashboard/applicants.html', locals())


@dashboard_login_required
def new_snippet(request):
    form = SnippetForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse('dashboard:snippets'))

    return render(request, 'dashboard/edit_snippet.html', locals())


@dashboard_login_required
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


@dashboard_login_required
def new_page(request):
    form = PageForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse('dashboard:pages'))

    return render(request, 'dashboard/edit_page.html', locals())


@dashboard_login_required
def update_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    form = PageForm(request.POST or None, instance=page)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse('dashboard:pages'))

    return render(request, 'dashboard/edit_page.html', locals())


@dashboard_login_required
def preview_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    print page.subject
    return render(request, 'home/customized_page.html', locals())


@dashboard_login_required
@csrf_exempt
def new_image(request):
    form = ImgForm(request.POST or None)

    if request.method == "POST":
        message = ''
        if form.is_valid():
            form.save()
            message = 'success'
        else:
            message = 'fail'
        return HttpResponse(message)
    else:
        raise Http404


def login_user(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', reverse('dashboard:index'))
            return redirect(next_url)
        else:
            message = "The username and password were incorrect."

    return render(request, 'dashboard/login.html', locals())
