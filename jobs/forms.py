from django import forms
from .models import JobOffer

class JobOfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = ['company_name','Email', 'package', 'designation', 'notice_period', 'work_location']
