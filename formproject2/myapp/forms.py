from django import forms
class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0)
    
    # class Meta:
    #     model=student
    #     fields = ['name', 'email', 'age']               
        