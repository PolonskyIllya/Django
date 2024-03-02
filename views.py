from django.shortcuts import render
from django.http import HttpResponse


def my_shop(request):
    return HttpResponse("Hello this is my own shop!")

def my_shop1(request):
    return HttpResponse("Hello this is second list!")
