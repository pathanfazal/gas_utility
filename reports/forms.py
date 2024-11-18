from django import forms
from .models import Report

class ReportGenerationForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'description', 'report_type']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Report name is required.")
        return name
