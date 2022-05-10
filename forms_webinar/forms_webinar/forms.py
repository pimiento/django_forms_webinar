from django import forms
from .models import NameModel

class MessageForm(forms.Form):
    message = forms.CharField(
        max_length=6,
        label="Послание"
    )

class NameForm(forms.ModelForm):
    slug = forms.CharField(max_length=10)
    class Meta:
        model = NameModel
        fields = ["name"]
        excludes = ["slug"]
