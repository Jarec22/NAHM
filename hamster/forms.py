from django import forms
from hamster.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username', 'password',)
		
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		# no additional fields should be affected by the user, thus they are excluded
		# we only need this form to create a user object within our database with
		# the fields required for the game
		fields = ()
		exclude = ['day','hour','item','health','picture','story','choice']