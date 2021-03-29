from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth



# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    createDate = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=70)
    text = models.TextField()
    likes = models.IntegerField()

    def __str__(self):
        return '%s %s %s likes %s' % (self.title, self.text, self.likes, self.createDate)
    def like(likes):
        likes = likes +1



