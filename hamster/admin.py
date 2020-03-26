from django.contrib import admin
from hamster.models import Choice, Story, UserProfile
# Register your models here.

admin.site.register(Choice)
admin.site.register(Story)
admin.site.register(UserProfile)
