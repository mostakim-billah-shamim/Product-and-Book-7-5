from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import *
from .models import *
from django.contrib import messages


def DashboardPage(request):
    pdata=ProductModel.objects.all()
    pcount=pdata.count()

    bdata=BookModel.objects.all()
    bcount=bdata.count()

    cont={
        'pdata':pdata, 'pcount':pcount, 'bdata':bdata, 'bcount':bcount
    }
    return render(request, 'pages/dashboard.html',cont)



def RegisterPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        con_password=request.POST.get('con_password')
        
        user_exist=UserModel.objects.filter(username=username).exists()
        email_exist=UserModel.objects.filter(email=email).exists()

        if user_exist or email_exist:
            messages.error(request, 'User or Email Already Exists. Try Another')
            return redirect('register') 
        if password != con_password:
            messages.error(request, 'Passowrd didnt match, try again')

        else:
            UserModel.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, 'User created successfully')
            return redirect('login')
        
    return render(request, 'auth/register.html')


def LoginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login Successfull')
            return redirect('dashboard')
        
    return render(request, 'auth/login.html')


def LogoutPage(request):
    logout(request)
    messages.warning(request, 'You are logged out!')
    return redirect('dashboard')




def ProductPage(request,id=None):
    try:
        data=ProductModel.objects.get(id=id)
    except ProductModel.DoesNotExist:
        data=None

    if request.method == "POST":
        form=ProductForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            product=form.save(commit=True)
            product.user=request.user
            product.save()
            if id:
                messages.success(request, 'Product Updated')
            else:
                messages.success(request, 'Product Added')
            return redirect('dashboard')
    else:
        form=ProductForm(instance=data)
    cont={'form':form}
    return render(request, 'pages/product.html', cont)

def ProductDeletePage(request,id):
    ProductModel.objects.get(id=id).delete()
    messages.warning(request, 'Product Deleted')
    return redirect('dashboard')




def BookPage(request,id=None):
    try:
        data=BookModel.objects.get(id=id)
    except BookModel.DoesNotExist:
        data=None

    if request.method == "POST":
        form=BookForm(request.POST, instance=data)
        if form.is_valid():
            book=form.save(commit=True)
            book.user=request.user
            book.save()
            if id:
                messages.success(request, 'Book Updated')
            else:
                messages.success(request, 'Book Added')
            return redirect('dashboard')
    else:
        form=BookForm(instance=data)
    cont={'form':form}
    return render(request, 'pages/book.html', cont)

def BookDeletePage(request,id):
    BookModel.objects.get(id=id).delete()
    messages.warning(request, 'Book Deleted')
    return redirect('dashboard')





















# Create your views here.
