from django.shortcuts import render ,HttpResponse
from . import urls
# Create your views here.
def index(request):
    # return HttpResponse("this is index")
    return render(request,'index.html')

def about(request):
    # return HttpResponse("this is about")
    return render(request,'aboutus.html')

def Srobot(request):
    return HttpResponse("Welcome to sodier robot section")        

def cyberWarfare(request):
    # return HttpResponse("this is cyber warfare")     
    return render(request,'cyber.html')

def Uav(request):
    # return HttpResponse("Welcome to Uav's Section")     
    return render(request,'uav.html')

