from .models import ConfirmPassword
from django import forms

class ConfForm(forms.ModelForm):
    class Meta:
        model = ConfirmPassword
        fields = "__all__"