from django.shortcuts import render
from django.http import HttpResponse
from.models import Product
# Create your views here.
def index(request):
    react=Product.objects.all()
    return render(request,'index.html',{'Product':react})
   # return HttpResponse("<h1>Hello welcome django</h1>")
def about(request):
    return HttpResponse("<h1>Dinumol</h1>")
