from ast import mod
from datetime import datetime
from turtle import title
from django.db import models
from django.db.models.fields import CharField


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=12)
    query=models.CharField(max_length=7)
    descself=models.TextField()
    desc=models.TextField()
    teacher=models.BooleanField(default=False)
    student=models.BooleanField(default=False)
    date=models.DateField()
    
    def __str__(self):
        return self.name

class Stories(models. Model):
    story_id = models.AutoField
    name = models.CharField (max_length=50)
    thought = models.CharField (max_length=300)
    image  =models.ImageField(upload_to="success/images", default="")
    def __str__(self):
        return self.name

class Gallery(models. Model):
    title=models.CharField(max_length=50)
    image  =models.ImageField(upload_to="gallery/images", default="")
    def __str__(self):
        return self.title

class Result(models. Model):
    title=models.CharField(max_length=50)
    image  =models.ImageField(upload_to="Result/images", default="")
    def __str__(self):
        return self.title

class Pdf(models.Model):
    pdf_id = models.AutoField
    title=models.CharField(max_length=30)
    pdf=models.FileField(upload_to="Question peper/pdf",default="")
    date=models.DateField()
    
    def __str__(self):
        return self.title

class Notice(models.Model):
    notice_id= models.AutoField
    title=models.CharField(max_length=50)
    notice = models.TextField()
    link= models.CharField(max_length=150,blank=True,null=True)
    pdf=models.FileField(upload_to="Notice/pdf",default="Not Available")
    date=models.DateField()

    def __str__(self):
        return self.title