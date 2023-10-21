from django.db import models

class StaffUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    staff_id = models.CharField(max_length=10, unique=True)
    name=models.CharField(max_length=100)
    address=models.TextField(default='enter address')
    role=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='staffImage')
    biodata=models.FileField(upload_to='resumes')
    join_date=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.username