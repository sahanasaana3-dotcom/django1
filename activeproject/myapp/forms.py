from django import forms
from myapp.models import feedback

class feedback(forms.modelform):
    class meta:
        model=feedback
        fields="__all__"
        