from django.db import models

# Create your models here.
class tbl_districts(models.Model):
    districts_name=models.CharField(max_length=50)

class tbl_adminreg(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)

class tbl_type(models.Model):
    type_name=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_districts,models.CASCADE)
    