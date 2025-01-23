from django import forms
from .models import Student

class StudentLogin(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('email','password1')

        

class StudentSignup(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password1'] != ['password2']:
            raise forms.ValidationError('passwords do not match')
        cd['password2']