from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def namegen(request):
    return HttpResponse(bytes("Hello world", "utf-8"))

