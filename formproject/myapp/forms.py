from django import forms
from myapp.models import Studentform
# class Studentform(forms.Form):
#     name=forms.CharField()
#     age=forms.IntegerField()
#     place=forms.CharField()
#     email=forms.EmailField()
#     dob=forms.DateField()
    
    
class Studentform(forms.ModelForm):
    class Meta:
        model=Studentform
        fields='__all__'