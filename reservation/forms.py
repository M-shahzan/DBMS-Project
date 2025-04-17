from django import forms
from .models import Reservation,restables

class reserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'date', 'people_count', 'table']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'table': forms.HiddenInput(),  # Hide table input (pre-filled)
        }

class tableForm(forms.ModelForm):
    class Meta:
        model = restables
        fields = ['table_num', 'capacity', 'status']