from django.urls import path

from to_do_list.views.to_do_list import home_view

urlpatterns = [
    path('', home_view)
]