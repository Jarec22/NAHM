import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NAHM.settings')

import django
django.setup()


import csv
from hamster.models import UserProfile, Story, Choice

with open('user.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = UserProfile.objects.get_or_create(
            user = row[0],
            day = row[1],
            location = row[2],

        )

#with open('story.csv') as f:
 #   reader = csv.reader(f)
  #  for row in reader:
   #     _, created = Story.objects.get_or_create(
    #        storyname = row[0],
     #       title = row[1],
      #      description = row[2],
       #     day = row[3],
        #    choice1 = row[4],
         #   choice2 = row[5],
          #  choice3 = row[6],
    #    )
        
#with open('choice.csv') as f:
 #   reader = csv.reader(f)
  #  for row in reader:
   #     _, created = Chpoce.objects.get_or_create(
    #        choicename = row[0],
     #       title = row[1],
      #      description = row[2],
       #     day = row[3],
        #    progress = row[4],
         #   result = row[5],
        #)