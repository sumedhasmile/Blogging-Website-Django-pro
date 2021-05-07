from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=13)
    address = models.TextField()
    branch = models.CharField(max_length=50, default="CS")
    roll_no = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class BlogModel(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, null=True)
    desc = models.TextField(null=True)
    date = models.DateField(null=True)
    long_desc = models.TextField(null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.title + " -- " + self.cat.name


class Like(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.usr.first_name


class UserComments(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, null=True)
    msg = models.TextField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.usr.first_name + " -- " + self.blog.title


class UserDetail(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mobile = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.usr.first_name
