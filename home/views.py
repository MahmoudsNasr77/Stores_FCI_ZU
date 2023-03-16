from django.shortcuts import render
from inventor.models import invntor
from django.contrib.auth.decorators import login_required
@login_required
def home_render(request):
    data=invntor.objects.order_by('-data','-time')[:10]
    return render(request,'home.html',{'data':data})
