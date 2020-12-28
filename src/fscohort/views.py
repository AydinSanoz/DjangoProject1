from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request) :
    return HttpResponse("<h1>Hi this is fscohort home Page<h1>")

def about_view(request):
    return HttpResponse("<h2>Hi this is fscohort about page <h2>")