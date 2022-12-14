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
        fields = ('username','password1','password2', 'genderUsr', 'birthUsr', 'telUsr', 'imgUsr', 'ubiUsr')


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
