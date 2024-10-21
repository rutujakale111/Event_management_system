from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  
        }