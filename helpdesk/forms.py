from django import forms
from django.contrib.auth.models import User
from .models import Ticket


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password'
        })
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
    )

    class Meta:

        model = User

        fields = [

            'first_name',
            'last_name',
            'username',
            'email'

        ]

        widgets = {

            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),

            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }),

        }

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password != confirm:

            raise forms.ValidationError(

                "Passwords do not match."

            )

        return cleaned_data
class TicketForm(forms.ModelForm):

    class Meta:

        model = Ticket

        fields = [

            'subject',
            'description',
            'priority'

        ]

        widgets = {

            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ticket Subject'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describe your problem'
            }),

            'priority': forms.Select(attrs={
                'class': 'form-control'
            }),

        }