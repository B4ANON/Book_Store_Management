from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('login_user',login_user,name="login_user"),
    path('logout_user',logout_user,name="logout_user"),
    path('register',register,name="register"),
    path('storeowner',storeowner,name="storeowner"),
    path('addbook',addbook,name="addbook"),
    path('addstore',addstore,name="addstore"),
]