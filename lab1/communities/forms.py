from django import forms
from .models import Communitie
class CommunitieForm(forms.ModelForm):
    class Meta:
        model = Communitie
        fields = ['title', 'description', 'slug', 'free', 'banner']