from django.db import models
from BPapp.models import face, cat, staff, hair, makeup, branch, Product
from django.db.models import CASCADE


class signp(models.Model):
    signname = models.CharField(max_length=50, null=True, blank=True)
    signemail = models.EmailField(max_length=100, null=True, blank=True)
    signpass = models.CharField(max_length=50, null=True, blank=True)
    signimage = models.ImageField(upload_to='profile', null=True, blank=True)


class lo(models.Model):
    signemail = models.EmailField(max_length=100, null=True, blank=True)
    signpass = models.CharField(max_length=50, null=True, blank=True)


class cart(models.Model):
    itemid = models.ForeignKey(
        Product, on_delete=CASCADE, null=True, blank=True)
    userid = models.ForeignKey(signp, on_delete=CASCADE, null=True, blank=True)


class order(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    userid = models.ForeignKey(signp, on_delete=CASCADE, null=True, blank=True)


class ordercart(models.Model):
    itemid = models.ForeignKey(face, on_delete=CASCADE, null=True, blank=True)
    userid = models.ForeignKey(signp, on_delete=CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

class checkoutm(models.Model):
    firstname = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    cardname = models.CharField(max_length=50, null=True, blank=True)
    cardnumber = models.IntegerField(null=True, blank=True)
    expmonth = models.IntegerField(null=True, blank=True)
    expyear = models.IntegerField(null=True, blank=True)
    cvv = models.IntegerField(null=True, blank=True)

class chkp(models.Model):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)

class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to='profile', null=True, blank=True)
    def __str__(self):
        return self.caption