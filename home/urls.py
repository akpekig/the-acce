from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("looksgood", views.template_test, name="Template test"),
]
