import csv

with open('user.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = UserProfile.objects.get_or_create(
            user = row[0],
            day = row[1],
            picture = 'default.jpg',
            location = row[2],
            choicename = row[3],
        )

with open('story.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Story.objects.get_or_create(
            storyname = row[0],
            title = row[1],
            description = row[2],
            day = row[3],
            choice1 = row[4],
            choice2 = row[5],
            choice3 = row[6],
        )
        
with open('choice.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Chpoce.objects.get_or_create(
            choicename = row[0],
            title = row[1],
            description = row[2],
            day = row[3],
            progress = row[4],
            result = row[5],
        )
