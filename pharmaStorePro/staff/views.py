from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from accounts.models import *
from .forms import CategoryForm
from .forms import MedicineForm
# Create your views here.

def staffhome(request):
    p = StaffUser.objects.all()
    return render(request,'staffhome.html',{'p':p})

def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES)  # add request.FILES (THIS IS WHY image doesnt store)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')  # Redirect to the appropriate URL
    else:
        form = MedicineForm()
    
    return render(request, 'medi_add.html', {'form': form})


def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medi_list.html', {'medicines': medicines})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    
    return render(request, 'cate_add.html', {'form': form})

def category_list(request):
    categories = category.objects.all()
    return render(request, 'cate_list.html', {'categories': categories})

# def staff_pro(request,id):
#     obj1=get_object_or_404(StaffUser,pk=id)
#     return render(request,'staff_profile.html',{'p':obj1})
