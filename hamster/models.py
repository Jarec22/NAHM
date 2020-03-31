from django.db import models
from django.contrib.auth.models import User

#attribute explanations
#choicename - unique id which is equal to the owner story storyname, without the first character and with a character appended at the end F,S,T for first, second, third respectively
#title - the title of the choice displayed to the user
#description - a brief description of the choice
#day - on which day of the story is the choice taking place, could technically be deleted
#progress - the ID(the storyname) of the story to which the specific choice leads
#result - the text giving the consequences of the choice to the user
class Choice(models.Model):
    choicename = models.CharField(max_length=30, unique=True)
    title = models.TextField()
    description = models.TextField()
    day = models.IntegerField(default = 0)
    progress = models.TextField(default = 0)
    result = models.TextField(default = 0)
    
    def __str__(self):
        return self.choicename

#storyname - unique ID composed like this:
	#{character} - a unique character that would differ between different stories {1 number} - day {2 numbers} - the hours {2 numbers} - the minutes {2 numbers} - the users HP
	#this could be expanded to provide for more stories, and the helper function in the view could be expanded to accomodate this too. both of these relatively easy
#title - the title of the story visible to the user
#description - describes the current situation to the user
#day - which day of the story arc it is
class Story(models.Model):
    storyname = models.CharField(max_length=30, unique=True)
    title = models.TextField()
    description = models.TextField()
    day = models.IntegerField(default = 0)
    choice1 = models.ForeignKey(Choice, on_delete=models.PROTECT, related_name='choice1', null=True)
    choice2 = models.ForeignKey(Choice, on_delete=models.PROTECT, related_name='choice2', null=True)
    choice3 = models.ForeignKey(Choice, on_delete=models.PROTECT, related_name='choice3', null=True)
    
    def __str__(self):
        return self.storyname

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    day = models.IntegerField(default = 0)
    picture = models.ImageField(blank = True, upload_to='profile_pics', default='default.jpg')
    location = models.TextField(default = 0)
    choicename = models.TextField(default = 0)
    def __str__(self):
        return self.user.username



# Create your models here.
