from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    plan = models.CharField(max_length=50, default='free')
    

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300, default='No description')
    image = models.ImageField(upload_to='images/', null=True)
    # added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.IntegerField(default=0)
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)

class Tag(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
class CourseCategory(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Moderator(User):
    is_moderator = models.BooleanField(default=False)

class Student(User):
    is_student = models.BooleanField(default=True)
    courses = models.ManyToManyField(Course)

# Moderator on Course m-m relationship
class Moderator_Course(models.Model):
    moderator = models.ForeignKey(Moderator, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    up_vote = models.BooleanField(default=True)
    voted_at = models.DateTimeField(auto_now_add=True)

