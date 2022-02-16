from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'views.html')
def link(request):
    result=str(request.GET['message'])




    return render(request, 'reversed.html',{'message':result})


