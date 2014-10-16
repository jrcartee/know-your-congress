# Django Imports
from django import forms
from django.contrib.auth import get_user_model, authenticate
# REST Imports
from rest_framework.authtoken.models import Token
# Internal Imports
User = get_user_model()


class LoginForm(forms.Form):
    """ Authorizes a user's credentials
    """
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    err_set = {
        'no_auth': "Couldn't find that combination",
        'inactive': "This account is not enabled"
    }

    def clean(self):
        if len(self.errors) == 0:
            self.user = self.auth_user()
            if self.user is None:
                raise forms.ValidationError(self.err_set['no_auth'])
            elif not self.user.is_active:
                raise forms.ValidationError(self.err_set['inactive'])
        return self.cleaned_data

    def auth_user(self):
        email = self.cleaned_data['email']
        email = email.lower()
        return authenticate(
            email=email,
            password=self.cleaned_data['password']
        )

    def get_token(self):
        return Token.objects.get(user__pk=self.user.pk).key


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    err_set = {
        'exists': 'That email already exists in our records',
        'match': "The two passwords don't match"
    }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email = email.lower()

        User = get_user_model()
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError(self.err_set['exists'])
        return email

    def clean(self):
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError(self.err_set['match'])
        return self.cleaned_data

    def save(self):
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password2'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        token = Token.objects.create(user=user)
        return token.key
