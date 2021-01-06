from django import forms

from .models import registration

class RegistrationForm(forms.ModelForm):
    
    class Meta:
        model = registration
        fields = ('name_of_the_participant', 'event','college','branch','semester')