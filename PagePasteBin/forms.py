from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

from django import forms
from .models import User

class TaskItemForm(forms.ModelForm):
    widgets = {
        'user': forms.HiddenInput,
    }

    class Meta:
        model = User
        fields = ('user_name', 'email')