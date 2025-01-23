from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Student(AbstractUser):
    name = models.CharField(max_length=350, help_text='name of student',null=True,blank=True)
    email = models.EmailField(max_length=20, help_text='email of student')
    phonenumber = models.IntegerField( help_text='phonenumber of student',null=True,blank=True)
    username=models.CharField(null=True,blank=True,max_length=50,unique=True)
    student_id = models.CharField(max_length=11, help_text='student id')
    gender_choices = (
        ('male','male'),
        ('female','female'),
        ('others', 'others')
        )
    gender = models.CharField(max_length=10, choices = gender_choices)
    password1 = models.CharField(max_length=100, help_text="create a strong password")
    password2 = models.CharField(max_length=100, help_text="confirm password")

    # USERNAME_FIELD=username
