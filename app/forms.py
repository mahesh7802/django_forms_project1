from django import forms
d=[('male','MALE'),('female','FEMALE')]
class Registration(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    father_name=forms.CharField(max_length=100)
    gender=forms.ChoiceField(choices=d)
    date_of_birth=forms.DateField()
    mobile_no=forms.IntegerField()
    email=forms.EmailField(max_length=100)
    
