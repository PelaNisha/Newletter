from django.shortcuts import render
from .models import post
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
class HomeView(ListView):
    model = post
    template_name = 'base.html'

    def get_queryset(self):
      return post

class NewsDetailView(DetailView):
    model = post
    template_name = 'new_details.html'
    

class AddNewView(CreateView):
    model = post
    template_name = 'addpost.html'
    fields = '__all__'
    

def post(request):
    return render(request, 'addpost.html')    




def post1(request):
    return render(request, '1.html')    
