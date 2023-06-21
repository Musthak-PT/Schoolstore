from django.db import models


# Create your models here.
# class register(models.Model):
class Formregister(models.Model):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    address = models.TextField()
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    phoneno = models.CharField(max_length=12)
    email = models.EmailField()
    dept = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    purpose = models.CharField(max_length=250)
    # materials = models.CharField(max_length=250)

    def __str__(self):
        return self.fname


class Login(models.Model):
    uname = models.CharField(max_length=250)
    pswd = models.CharField(max_length=250)

    def __str__(self):
        return self.fname


