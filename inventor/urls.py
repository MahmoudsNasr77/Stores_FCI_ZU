app_name="inventor"
from django.urls import path
from . import views

urlpatterns = [
    path('',views.invtory_render,name="invtory_render"),
     path('/add', views.add, name='add'),
      path('/quntity', views.quntity, name='quntity'),
]