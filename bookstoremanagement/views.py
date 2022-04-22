from ast import IsNot
from pyexpat.errors import messages
from urllib import response
import django
from bookstoremanagement.models import Store,Book
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout




# Create your views here.
def home(request):
    allbooks = Book.objects.all()
    context = {'allbooks':allbooks}
    print(allbooks)
    return render(request,'home.html',context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        loginpass = request.POST['loginpass']

        user = authenticate(request, username=username,password=loginpass)
        
        if user is not None:
            login(request,user)
            return redirect('storeowner')
        else:
            return redirect('register')
    else:
        return render(request,'login_user.html')

def logout_user(request):
    logout()
    return redirect('home')

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        passwd = request.POST['passwd']
        new_user = User.objects.create_user(username,email,passwd)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.save()
        return redirect('home')
    else:
        return render(request,'register.html')

def storeowner(request):
    return render(request,'storeowner.html')

def addstore(request):
    if request.method == 'POST':
        sname = request.POST['sname']
        city = request.POST['city']
        newstore=Store(store_title=sname,store_city=city)
        newstore.save()
        return HttpResponse('successful')
    else:
        return render(request,'addstore.html')

def addbook(request):
    if request.method == 'POST':
        bname = request.POST['bname']
        aname = request.POST['aname']
        quantity = request.POST['quantity']
        newbook=Book(book_title=bname,book_author=aname,book_stock=quantity)
        newbook.save()
        return HttpResponse('successful')
    else:
        return render(request,'addbook.html')