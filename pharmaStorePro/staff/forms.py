from django import forms
from .models import Medicine,category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ['name']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name','cat_id','brand_id','image','price','details','use']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     # Add Bootstrap classes directly to form fields
    #     self.fields['name'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['cat_id'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['brand_id'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['image'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['price'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['details'].widget.attrs.update({'class': 'form-control form-control-sm'})
    #     self.fields['use'].widget.attrs.update({'class': 'form-control form-control-sm'})