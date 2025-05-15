from django.db import models
from home.models import restables
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to Django User model
    table = models.ForeignKey(restables, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    people_count = models.IntegerField(null=True, blank=True)
    res_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key

    class Meta:
        db_table = 'reservations'  # Ensures Django uses the correct database table

    def __str__(self):
        return f"Reservation {self.res_id} for {self.name} at Table {self.table.table_num}"
    
    
class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    rating = models.IntegerField()
    visit_date = models.DateField()
    comments = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'feedback'  # Matches your MySQL table name

