from django.shortcuts import redirect, render
from django.urls import reverse
from .models import invntor
from .form import Addquntity
def invtory_render(request):
    data=invntor.objects.all().order_by('-data')
    context={"data":data}
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
def quntity(request):
    return render(request,'quntity.html')