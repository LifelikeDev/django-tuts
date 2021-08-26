from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # name = "Humphrey"
    context = {
        'name': 'Meghan Markle',
        'age': 42,
        'height': 145.8,
        'nationality': 'Canada'
    }

    return render(request, "index.html", context)

