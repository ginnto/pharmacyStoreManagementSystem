from django.shortcuts import render, get_object_or_404
from staff.models import *
# Create your views here.


def home(request,c_slug=None):
    if c_slug  != None:
        print(c_slug)
        c_page=get_object_or_404(category,slug=c_slug) # c_page=men
        print(c_page)
        medi=Medicine.objects.filter(cat_id=c_page) 
        print(medi)
    else:
        print('haiii')
        medi=Medicine.objects.all()


   
    return render(request,'index.html',{'med': medi})


def detail(request,c_slug,product_slug):
    prodt=Medicine.objects.get(cat_id__slug=c_slug,slug=product_slug)
    return render(request,'single-product.html',{'pr':prodt})

