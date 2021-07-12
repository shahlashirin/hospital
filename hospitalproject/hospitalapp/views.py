from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def fun(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")

def blogsingle(request):
    return render(request,"blog-single.html")

def contact(request):
    return render(request,"contact.html")

def doctors(request):
    return render(request,"doctors.html")

def detail(request):
    return render(request,"blog-single.html")

def dermatology(request):
    return render(request,"dermatology.html")

def gynaecology(request):
    return render(request,"gynaecology.html")

def cardiology(request):
    return render(request,"cardiology.html")

def nephrology(request):
    return render(request,"nephrology.html")

def orthology(request):
    return render(request,"orthology.html")