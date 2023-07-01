from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return HttpResponse("Hello World")

@login_required(login_url='')
def dashboard(request):
    return render(request, 'dashboard/index.html')

def homePageView(request):
    if request.user.is_authenticated:
        return dashboard(request)
    else:
        return home(request)
