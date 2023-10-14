from django.shortcuts import render,redirect
from item.models import Category,Item
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from item.forms import ItemForm
from django.contrib.auth.decorators import login_required

def index(request):
    items=Item.objects.filter(is_sold=False)
    categories=Category.objects.all()
    
    return render(request,'index.html',
                  {
                      'items':items,
                   'categories':categories})

def detail(request,pk,category):
    Category.objects.get(name=category)
    item=Item.objects.get(id=pk)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(id=pk)[0:4]
    return render(request,'detail.html',{'item':item,'category':category,'related_items':related_items})

def signup(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nukes:login')

    
    form=UserForm()
    return render(request,'signup.html',{'form':form})

def logins(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.cleaned_data.get('username')
            passw=form.cleaned_data.get('password')
            userlog=authenticate(username=user,password=passw)
            if userlog is not None:
                login(request,userlog)
                return redirect('nukes:index') 

    form=AuthenticationForm(request,data=request.POST)
    return render(request,'login.html',{'form':form})

def logouts(request):
    logout(request)
    return redirect('nukes:index')

@login_required
def create_item(request):
    if request.method=="POST":
        form=ItemForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.cleaned_data.get('image')
            print(image)
            form.save()
            return redirect('dashboard:index')

    
    form=ItemForm()
    return render(request,'create.html',{'form':form})

def contact(request):
    return render(request,'contact.html')
  