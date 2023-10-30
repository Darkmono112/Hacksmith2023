from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator
from DroneConesApp.models import FAQ


class CreateUserForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17, required=False)

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True  # Make 'email' field required
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone Number'
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-input'
            required = "*" if visible.field.required else ""
            # Phone number is weird, so it is a special case
            visible.field.widget.attrs['placeholder'] = f"{visible.field.label if visible.field.label else self.fields['phone'].widget.attrs['placeholder']}" + required
            

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AddDroneForm(forms.Form):
    size = forms.ChoiceField(
        choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')],
        label='Size',
        required=True,
    )

    active = forms.ChoiceField(
        choices=[('active', 'Active'), ('inactive', 'Inactive')],
        label='Status',
        required=True,
    )

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']