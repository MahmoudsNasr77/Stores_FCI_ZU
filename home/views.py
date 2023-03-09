from django.shortcuts import render
from inventor.models import invntor
from django.contrib.auth.decorators import login_required
@login_required
def home_render(request):
    data=invntor.objects.all()
    return render(request,'home.html',{'data':data})
