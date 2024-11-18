from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'file_attachment']  # Fields from the model

# Form to filter service requests
class ServiceRequestFilterForm(forms.Form):
    status_choices = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    status = forms.ChoiceField(choices=status_choices, required=False)
