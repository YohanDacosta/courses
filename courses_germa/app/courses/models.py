from django.db import models

# Create your models here.

class Schedule(models.Model):
    initial_date = models.DateTimeField()
    final_date = models.DateTimeField()
    
class Price(models.Model):
    normal = models.FloatField()
    institution = models.FloatField()
    
class Duration(models.Model):
    week_duration = models.IntegerField()
    quantity_lesson_x_week= models.IntegerField()
    minutes = models.FloatField()
    total_lessons = models.IntegerField()

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    level = models.CharField(max_length=30)
    days_week = models.IntegerField()
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    duration_course = models.ForeignKey(Duration, on_delete=models.CASCADE)
    quantity_persons = models.IntegerField()
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    initial_date = models.DateTimeField()
    final_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_created=True, auto_now=True)
    registration_deadline = models.DateTimeField()
    goal = models.TextField()
    

    
