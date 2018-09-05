from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

def  visit(request):
    return HttpResponse("hello customer")