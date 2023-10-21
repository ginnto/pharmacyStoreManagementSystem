from django.urls import path
from . import views

urlpatterns=[
    path('staffhome',views.staffhome,name="staffhome"),
    path('add_medicine',views.add_medicine,name="add_medicine"),
    path('add_category',views.add_category,name="add_category"),
    path('medicine_list',views.medicine_list,name="medicine_list"),
    path('category_list',views.category_list,name="category_list"),
    # path('<int:id>',views.staff_pro,name="staffprofile"),
]

