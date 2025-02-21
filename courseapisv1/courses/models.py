from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class ModelBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='courses/%Y/%m/',
                          null=True, blank=True)
    class Meta:
        abstract = True
        ordering = ['-id']
class Category(ModelBase):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Course(ModelBase):
    subject = models.CharField(max_length=255, unique= True)
    desciption = models.CharField(max_length=255, unique= True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.subject


class Lesson(ModelBase):
    class Meta:
        unique_together = ('subject', 'course')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE,)
    def __str__(self):
        return self.subject




