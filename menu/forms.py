from django import forms
from .models import Menu

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['dish_name', 'type', 'dish_price']

class DeleteItemForm(forms.Form):
    delete_dish_name = forms.CharField(max_length=255, label="Dish Name")