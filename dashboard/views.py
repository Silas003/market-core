from django.shortcuts import render,redirect
from item.models import  Item,Category
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    items=Item.objects.filter(created_by=request.user)
    return render(request,'dash.html',{'items':items})

@login_required
def delete(request,category,pk):
    category=Category.objects.get(name=category)
    item=Item.objects.get(id=pk)
    item.delete()
    return redirect('dashboard:index')
    
