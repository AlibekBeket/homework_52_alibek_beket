from django.urls import path

from to_do_list.views.to_do_list import *

urlpatterns = [
    path('', home_view),
    path('to_do/add/', add_view)
]
