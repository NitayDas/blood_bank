from django import forms
from .models import Patient


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [ 'phone', 'division', 'dist', 'address', 'disease']
