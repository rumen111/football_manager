from django import forms
from .models import Tactic

class TacticForm(forms.ModelForm):
    class Meta:
        model = Tactic
        fields = ['title', 'formation', 'description']

