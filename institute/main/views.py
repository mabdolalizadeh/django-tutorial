from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

def index(request):
    response = render(request, 'main/index.html')
    return HttpResponse(response)