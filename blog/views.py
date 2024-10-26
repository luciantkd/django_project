from django.shortcuts import render
from django.http import HttpResponse

# how we want to handle routes

def home(request):
    return HttpResponse('<h1>Blog Home</1>')

def about(request):
    return HttpResponse('<h1>Blog About</1>')