from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

def  visit(request):
    print(request.META)
    return HttpResponse(request.META)
