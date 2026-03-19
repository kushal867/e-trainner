from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=4,
        max_length=150,
        strip=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Username",
            "class": "form-control",
            "autocomplete": "username"
        })
    )
    
    password = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "form-control",
            "autocomplete": "current-password"
        })
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.isalnum():
            raise forms.ValidationError("Username must be alphanumeric.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid username or password.")

            if not user.is_active:
                raise forms.ValidationError("This account is inactive.")

            # Store user for later use (optional)
            self.user = user

        return cleaned_data
