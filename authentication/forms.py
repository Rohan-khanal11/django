from django import forms
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='Username',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username',
            'class': 'form-control'
        })  
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'form-control'
        })
    )
    


class ProfileForm(forms.ModelForm):
   
    class Meta:
        model = Profile
        fields = ['user', 'dob', 'position']

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        if request:
            self.fields['user'].initial = request.user.username