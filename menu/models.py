from django.db import models

class Menu(models.Model):
    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=255, null=False)
    dish_price = models.IntegerField(null=False)
    type = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'menu'  # ✅ Tells Django to use the existing 'menu' table

    def __str__(self):
        return self.dish_name


