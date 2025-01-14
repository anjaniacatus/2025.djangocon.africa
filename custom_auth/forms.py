from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model


class CustomSignupForm(SignupForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        return user
