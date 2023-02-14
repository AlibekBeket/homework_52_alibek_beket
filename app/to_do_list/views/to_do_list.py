from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from to_do_list.models import ToDo


def home_view(request: WSGIRequest):
    if request.POST:
        to_do_add = {
            'description': request.POST.get('description'),
            'status': request.POST.get('status'),
            'created_at': request.POST.get('date')
        }
        ToDo.objects.create(**to_do_add)
    to_do_list = ToDo.objects.all()
    context = {
        'to_do_list': to_do_list
    }
    return render(request, 'home_page.html', context=context)


def add_view(request: WSGIRequest):
    return render(request, 'add_page.html')
