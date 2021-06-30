from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name ='home' ),
    path('newpost/', views.post, name = 'addpost'),
    path('newpost/01', views.post1, name = '01'),

]
