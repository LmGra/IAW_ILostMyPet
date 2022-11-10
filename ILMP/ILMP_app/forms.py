from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

#from .models import CustomUser

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2', 'genderUsr', 'birthUsr', 'telUsr', 'imgUsr', 'ubiUsr')
