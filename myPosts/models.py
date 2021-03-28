from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
    name = models.CharField(max_length=70)
    loginTime = models.DateField()



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createDate = models.DateField(auto_now=True)
    title = models.CharField(max_length=70)
    text = models.TextField()
    likes = models.IntegerField()
