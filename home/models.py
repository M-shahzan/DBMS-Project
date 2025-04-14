from django.db import models

# Create your models here.
class restables(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_num = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    class Status(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        RESERVED = 'reserved', 'Reserved'
        OCCUPIED = 'occupied', 'Occupied'

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.AVAILABLE
    )

    class Meta:
        db_table = 'restables'  # ✅ Tells Django to use the existing 'menu' table

    def __str__(self):
        return self.table_id