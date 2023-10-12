
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name= "blog"

urlpatterns = [
    path("", TemplateView.as_view(template_name="Blog/index.html") , name="index"),
    path("blogcategoria/list/", views.BlogCategoriaList.as_view(), name="blogcategoria_list"), 
    path("blogcategoria/detail/<int:pk>", views.BlogCategoriaDetail.as_view(), name="blogcategoria_detail"), 

]