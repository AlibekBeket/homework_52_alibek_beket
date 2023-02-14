from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from to_do_list.models import ToDo


def home_view(request: WSGIRequest):
    to_do_list = ToDo.objects.all()
    context = {
        'to_do_list': to_do_list
    }
    return render(request, 'home_page.html', context=context)

def add_view(request: WSGIRequest):
    return render(request, 'add_page.html')
