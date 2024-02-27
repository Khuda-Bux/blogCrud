from django import forms
from .models import blog
class blogsign(forms.ModelForm):
    class Meta:
        model = blog
        fields=['title','dis']
        