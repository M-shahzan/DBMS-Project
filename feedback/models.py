from django.db import models

# Create your models here.
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

