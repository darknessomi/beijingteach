# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello Omi!')
    # return render(request, 'home/index.html')
