from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from indexapp.models import IPdata
def  visit(request):
    ip = request.META.get('REMOTE_ADDR')
    print(ip)
    all = IPdata.objects.all()
    # for item in request.META:
    #     print(item,request.META.get(item))
    return render(request, "test.html", {'current_user': all,'re_ip':ip})
#
# def add_IP(request):
#     for