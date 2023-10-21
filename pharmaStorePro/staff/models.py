from django.db import models
from home.models import brand
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=50) 
    slug=models.SlugField(max_length=200,unique=True)

    

    def save(self, *args, **kwargs):
        # Automatically generate the slug from the name field
        self.slug = slugify(self.name)
        super(category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
     
    def get_url(self):
        return reverse('home:prod_cat',args=[self.slug]) 

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    slug=models.SlugField(max_length=200,unique=True)
    cat_id = models.ForeignKey(category, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')  # Add this line
    price= models.IntegerField(default='0')
    stock= models.IntegerField(default='1')
    details=models.TextField(default='')
    use=models.TextField(default='')


    def save(self, *args, **kwargs):
        # Automatically generate the slug from the name field
        self.slug = slugify(self.name)
        super(Medicine, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse('home:detail',args=[self.cat_id.slug,self.slug])

