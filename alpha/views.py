from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature


def index(request):
    features = Feature.objects.all()
    return render(request, 'wordcounter.html', {"features": features})


# word counter function


def counter(request):
    words = request.POST['words']
    number_of_words = len(words.split())

    return render(request, 'countedwords.html', {'number_of_words': number_of_words})
