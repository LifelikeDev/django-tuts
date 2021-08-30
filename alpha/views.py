from django.shortcuts import render
from django.http import HttpResponse
from .models import Features


def index(request):
    feature1 = Features()
    feature2 = Features()
    feature3 = Features()
    feature4 = Features()

    feature1.id = 1
    feature1.title = "Easy to use"
    feature1.description = "As simple as ABC and \"I-can-see\""

    feature2.id = 2
    feature2.title = "Reliable"
    feature2.description = "Built to be trusted by many"

    feature3.id = 3
    feature3.title = "Secure"
    feature3.description = "Bonds that can never break"

    feature4.id = 4
    feature4.title = "Resilient"
    feature4.description = "Passed through the cold and the heat"

    features = [feature1, feature2, feature3, feature4]

    return render(request, 'wordcounter.html', {"features": features})


# word counter function


def counter(request):
    words = request.POST['words']
    number_of_words = len(words.split())

    return render(request, 'countedwords.html', {'number_of_words': number_of_words})
