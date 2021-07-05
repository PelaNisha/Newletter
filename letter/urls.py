from django.urls import path
from . import views
from . views import HomeView, NewsDetailView, AddNewView


urlpatterns = [
    path('',HomeView.as_view(), name ='home' ),
    # path('news/<int:pk>', NewsDetailView.as_view(), name = 'news_detail'),
    path('addNews/', AddNewView.as_view(), name = 'addnews'),


]
