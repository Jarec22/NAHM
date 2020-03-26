from django.db import models
from django.contrib.auth.models import User

class Choice(models.Model):
    choicename = models.CharField(max_length=30, unique=True)
    title = models.TextField()
    description = models.TextField()
    day = models.IntegerField()
    hour = models.IntegerField()
    item = models.IntegerField()
    health = models.IntegerField()
    
    def __str__(self):
        return self.choicename

class Story(models.Model):
    storyname = models.CharField(max_length=30, unique=True)
    title = models.TextField()
    description = models.TextField()
    day = models.IntegerField()
    hour = models.IntegerField()
    item = models.IntegerField()
    health = models.IntegerField()
    choice1 = models.ForeignKey(Choice, on_delete=models.PROTECT, related_name='choice1', null=True)
    choice2 = models.ForeignKey(Choice, on_delete=models.PROTECT, related_name='choice2', null=True)
    choice3 = models.ForeignKey(Choice, on_delete=models.PROTECT, related_name='choice3', null=True)
    
    def __str__(self):
        return self.storyname

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    day = models.IntegerField(default = 0)
    hour = models.IntegerField(default = 0)
    item = models.IntegerField(default = 0)
    health = models.IntegerField(default = 0)
    picture = models.ImageField(blank = True)
    story = models.ManyToManyField(Story, blank = True)
    choice = models.ManyToManyField(Choice, blank = True)

    def __str__(self):
        return self.user.username



# Create your models here.
