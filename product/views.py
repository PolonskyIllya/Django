from django.shortcuts import render
from django.http import HttpResponse


def my_product(request):
    return HttpResponse("Hi this is my product!")

def my_product1(request):
    return HttpResponse("Hi this is second list!")
