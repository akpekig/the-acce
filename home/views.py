from django.shortcuts import render
from django.views import generic


def index(request):
    return render(
        request,
        "index.html",
    )

def template_test(request):
    return render(
        request,
        "test.html",
    )
