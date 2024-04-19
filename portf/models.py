from django.db import models


# Create your models here.
class Personal(models.Model):
    pers_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='img/')
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    desc = models.TextField()
    age = models.CharField(max_length=5)
    facebook_url = models.URLField(max_length=255, blank=True, null=True)
    insta_url = models.URLField(max_length=255, blank=True, null=True)
    email_add = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, null=True)
    col_year = models.CharField(max_length=50, null=True)
    col_sch = models.CharField(max_length=50, null=True)
    shs_year = models.CharField(max_length=50, null=True)
    shs_sch = models.CharField(max_length=50, null=True)
    jhs_year = models.CharField(max_length=50, null=True)
    jhs_sch = models.CharField(max_length=50, null=True)
    ele_year = models.CharField(max_length=50, null=True)
    ele_sch = models.CharField(max_length=50, null=True)

class Website(models.Model):
    web_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='web/')
    title = models.TextField(null=True)


class Art(models.Model):
     art_id = models.AutoField(primary_key=True)
     image = models.ImageField(upload_to='art/')
     descr = models.TextField()

class Doh(models.Model):
     art_id = models.AutoField(primary_key=True)
     image = models.ImageField(upload_to='doh/')
   






