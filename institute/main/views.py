from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def signin(request):
    return render(request, 'main/signin.html')