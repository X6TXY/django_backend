from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse("home")


def products(request):
    return HttpResponse("products")


def customer(request):
    return HttpResponse("customer")
