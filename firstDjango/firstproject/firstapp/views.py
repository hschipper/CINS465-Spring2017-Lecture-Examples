from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'title':"Home",
        'content': "Goodbye World"
        }
    return render(request,'home.html',context)
