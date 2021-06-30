from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')


def post(request):
    return render(request, 'addpost.html')    




def post1(request):
    return render(request, '1.html')    
