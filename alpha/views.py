from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature


def index(request):
    features = Feature.objects.all()
    return render(request, 'wordcounter.html', {"features": features})


def counter(request):
    words = request.POST['words']
    number_of_words = len(words.split())

    return render(request, 'countedwords.html', {'number_of_words': number_of_words})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password_one = request.POST['password1']
        password_two = request.POST['password2']

        if password_one == password_two:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email has been used')
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username has been taken')
                return redirect('register')

            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password_one)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'The information you entered is invalid')
            return redirect('login')

    else:
        return render(request, 'login.html')
