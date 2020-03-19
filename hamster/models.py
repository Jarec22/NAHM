from django.db import models

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
    choice1 = models.ForeignKey(Choice, on_delete=models.PROTECT)
    choice1 = models.ForeignKey(Choice, on_delete=models.PROTECT)
    choice1 = models.ForeignKey(Choice, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.storyname

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    day = models.IntegerField()
    hour = models.IntegerField()
    item = models.IntegerField()
    health = models.IntegerField()
    picture = models.ImageField()
    story = models.ManyToManyField(Story)
    choice = models.ManyToManyField(Choice)

    def __str__(self):
        return self.username



# Create your models here.
