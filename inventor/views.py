from django.shortcuts import render
from datetime import datetime, timedelta
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import invntor,items,paydata
from .form import Addquntity,pay_request
from django.core.paginator import Paginator

def invtory_render(request):
    
    data=invntor.objects.order_by('-data','-time')
    paginator = Paginator(data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"data":page_obj}
    return render(request,'inventor.html',context)
def add(request):
    if request.method=='POST':
        Addquntity_form=Addquntity(request.POST)
        if Addquntity_form.is_valid():
            myform=Addquntity_form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect('inventor:invtory_render')
    else:
        Addquntity_form=Addquntity()    
    return render(request,'add.html',{'Addquntity_form':Addquntity_form})
def pay_data(request):
    pay_request_form=pay_request()
    if request.method=='POST':
        pay_request_form=pay_request(request.POST)
        if pay_request_form.is_valid():
            myform=pay_request_form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect('inventor:previous_request_list')
   
    return render(request,'pay.html',{'pay_request_form':pay_request_form})
def previous_request_list(request):
    paydatalist=paydata.objects.order_by('-data','-time')
    paginator = Paginator(paydatalist, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'previous_request_list.html',{'paydatalist':page_obj})

def previous_request(request,id):
    previous_request=paydata.objects.get(id=id)
    return render(request,'previous_request.html',{'previous_request':previous_request})

def quntity(request):

    totalquntity=items.objects.all()
    paginator = Paginator(totalquntity, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'quntity.html',{'quntity':page_obj})

def year_item(request):
    last_day = datetime.today() - timedelta(days=365)
    data = invntor.objects.filter(data__gte=last_day)
    paginator = Paginator(data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'year.html',{'data':page_obj})
def month_item(request):
    last_day = datetime.today() - timedelta(days=30)
    data = invntor.objects.filter(data__gte=last_day)
    paginator = Paginator(data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'month.html',{'data':page_obj})

def day_item(request):
    last_day = datetime.today() - timedelta(days=1)
    data = invntor.objects.filter(data__gte=last_day)
    paginator = Paginator(data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'day.html', {'data': page_obj})
