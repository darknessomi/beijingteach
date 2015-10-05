from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def experience(request):
    return render(request, 'home/experience.html')


def china(request):
    return render(request, 'home/china.html')


def accommodations(request):
    return render(request, 'home/accommodations.html')


def contact(request):
    return render(request, 'home/contact.html')

def apply(request):
    return render(request, 'home/apply.html')
