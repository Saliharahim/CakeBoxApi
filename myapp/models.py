from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Occations(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Cake(models.Model):
    name=models.CharField(max_length=200)
    occation=models.ForeignKey(Occations,on_delete=models.CASCADE)
    options=(("round","round"),
            ("square","square"),
            ("heart","heart"),
            ("rectangle","rectangle"))
    shape=models.CharField(max_length=150,choices=options,default="round")
    layer=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    weight=models.PositiveIntegerField()

    def __str__(self):
        return self.name

class CakeImage(models.Model):
    cake=models.ForeignKey(Cake,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="cakeimages",null=True,blank=True)

class Cart(models.Model):
    cake=models.ForeignKey(Cake,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    cake=models.ForeignKey(Cake,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=250)
    status=models.BooleanField(default=False)
    expected_delivery_date=models.DateTimeField()

class Reviews(models.Model):
    cake=models.ForeignKey(Cake,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=100)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.cake
