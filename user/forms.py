from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=4,
        max_length=150,
        strip=True,
        label=_("Username"),
        widget=forms.TextInput(attrs={
            "placeholder": "Username",
            "class": "form-control",
            "autocomplete": "username"
        })
    )

    password = forms.CharField(
        min_length=6,
        label=_("Password"),
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "form-control",
            "autocomplete": "current-password"
        })
    )

    error_messages = {
        "invalid_login": _("Invalid username or password."),
        "inactive": _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        Accept request for advanced use (sessions, IP logging, etc.)
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and not username.isalnum():
            raise forms.ValidationError(_("Username must be alphanumeric."))
        return username

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password
            )

            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages["invalid_login"],
                    code="invalid_login"
                )

            self.confirm_login_allowed(self.user_cache)

        return cleaned_data

    def confirm_login_allowed(self, user):
        """
        Control login rules (extensible)
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages["inactive"],
                code="inactive"
            )

    def get_user(self):
        return self.user_cache
