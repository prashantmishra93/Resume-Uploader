from django import forms
from .models import ResumeUpload

sex = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

speech = (
    ('Hindi', 'Hindi'),
    ('English', 'English'),
    ('Other', 'Other')
)

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=sex, widget=forms.RadioSelect())
    language = forms.ChoiceField(choices=speech, widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = ResumeUpload
        fields = "__all__"
        labels = {'name':'Full Name', 'dob':'Date of Birth', 'father':'Father Name', 'mother':'Mother Name',
                  'profile_img':'Profile', 'pin':'Pin Code', 'sivling':'Siblings'}
        widgets = {               #it is use for also add bootstrap class
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sivling': forms.TextInput(attrs={'class': 'form-control'}),
            'father': forms.TextInput(attrs={'class': 'form-control'}),
            'mother': forms.TextInput(attrs={'class': 'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'education':forms.Select(attrs={'class':'form-control'}),
            'skill':forms.Select(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
        }