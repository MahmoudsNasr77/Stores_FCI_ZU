app_name="inventor"
from django.urls import path
from . import views

urlpatterns = [
    path('',views.invtory_render,name="invtory_render"),
     path('/add', views.add, name='add'),
      path('/quntity', views.quntity, name='quntity'),
      path('/pay_data', views.pay_data, name='pay_data'),
    path('/previous_request_list', views.previous_request_list, name='previous_request_list'),
     path('/previous_request_list/<int:id>', views.previous_request, name='previous_request'),
    path('/year', views.year_item, name='year_item'),
    path('/month', views.month_item, name='month_item'),
path('/day', views.day_item, name='day_item'),  
]