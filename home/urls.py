from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('<str:category>', views.category, name = "category"),
    path('post/<int:id>', views.post, name = "post")
    
] 
