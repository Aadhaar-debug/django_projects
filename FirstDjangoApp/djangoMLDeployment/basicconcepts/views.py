from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def User(request):
    username = request.GET['username']
    print(username)
    return render(request, 'user.html',{'name':username})