from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # name = "Humphrey"
    # context = {
    #     'name': 'Meghan Markle',
    #     'age': 42,
    #     'height': 145.8,
    #     'nationality': 'Canada'
    # }

    return render(request, 'wordcounter.html')


# word counter function


def counter(request):
    words = request.POST['words']
    number_of_words = len(words.split())

    return render(request, 'countedwords.html', {'number_of_words': number_of_words})
