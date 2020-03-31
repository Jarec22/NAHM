from django.shortcuts import render, redirect
from django.http import HttpResponse
from hamster.forms import UserForm, UserProfileForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from hamster.models import Story, Choice, User
from django.http import JsonResponse

def choice(request):
	current_user = request.user.userprofile
	context_dict = {}
	#get which choice was selected so we can display it
	context_dict['choice'] = Choice.objects.get(choicename=current_user.choicename)
	#if the method was post the request came from the form on the website,
	#redirect back to the story page
	if request.method == "POST":
		return redirect(reverse("hamster:story"))
	#if not display the choice set in the context_dict
	return render(request, 'hamster/choice.html', context=context_dict)
	
def reset(request):
	context = {}
	#changes the value of users location to 0, none of the stories have storyname 0
	#which is the value used for this attribute. in another view a check is performed 
	#for 0, which if true sets the user location to the starting point of the story
	#if not it keeps the users location as it is - this saves the user attributes 
	#and progression between logins.
	current_user = request.user.userprofile
	current_user.location = 0
	current_user.save()
	return redirect(reverse("hamster:my_account"))

def story(request):
	context_dict = {}
	current_user = request.user.userprofile
	story = Story.objects.get(storyname=current_user.location)
	#if request comes from one of the forms on the site, i.e. POST
	#check which form it came from then set the location of the 
	#user to the next progression within the story and also set
	#the choicename attribute for the next view (choice) to display
	if request.method == "POST":
		if request.POST.get('choice1'):
			current_user.location = story.choice1.progress
			current_user.choicename = story.choice1.choicename
			current_user.save()
			story = Story.objects.get(storyname=current_user.location)
			return redirect(reverse("hamster:choice"))
		if request.POST.get('choice2'):
			current_user.location = story.choice2.progress
			current_user.choicename = story.choice2.choicename
			current_user.save()
			story = Story.objects.get(storyname=current_user.location)
			return redirect(reverse("hamster:choice"))
		if request.POST.get('choice3'):
			current_user.location = story.choice3.progress
			current_user.choicename = story.choice3.choicename
			current_user.save()
			story = Story.objects.get(storyname=current_user.location)
			return redirect(reverse("hamster:choice"))
	#parse user attributes from the location string (helper function at the bottom)
	#pass these in the context_dict so they can be displayed in this view
	values = get_story_vals(current_user.location)
	context_dict = values
	#check whether the current story has any choices if not do not add them to the 
	#context_dict. If they were added zero's would be displayed
	if story.choice1.title != "0":
		context_dict['choice1'] = story.choice1
		context_dict['choice2'] = story.choice2
	else:
		context_dict['end'] = True
	if story.choice3.title != "0":
		context_dict['choice3'] = story.choice3
	context_dict['story'] = story
	return render(request, 'hamster/story.html', context=context_dict)
	

def about(request):
	context_dict={}
	return render(request, 'hamster/about.html', context=context_dict)

#this view orders the story objects by day attribute, the first story in an arc will have day set to 0
#for different arc the character at the beginning of the storyname could be checked and compared
def index(request):
	current_user = request.user.userprofile
	story1 = Story.objects.order_by('day')[0]
	context_dict={}
	context_dict['story1'] = story1
	if request.method == 'POST':
		if request.POST.get('story1'):
			#this checks if the user has any 'save' data, i.e information about story progression from previous playthroughs
			if current_user.location == "0":
				current_user.location = story1.storyname
				current_user.save()
			return redirect(reverse('hamster:story'))
	
	return render(request, 'hamster/index.html', context=context_dict)
	
def faq(request):
	context_dict={}
	return render(request, 'hamster/faq.html', context=context_dict)
	
def contacts(request):
	context_dict={}
	return render(request, 'hamster/contacts.html', context=context_dict)

def start(request):
	
	registered = False
	
	if request.method == 'POST':
		# Check if the request came from the register button
		# if so handle it using the register logic and return
		# the user to the same page where they can login afterwards
		if request.POST.get('submit') == 'Register':
			user_form = UserForm(request.POST)	
			profile_form = UserProfileForm(request.POST)
			if user_form.is_valid() and profile_form.is_valid():
				user = user_form.save()
				user.set_password(user.password)
				user.save()
				profile = profile_form.save(commit=False)
				profile.user = user
				profile.save()
				registered = True
			else:
				print("user form err ", user_form.errors)
				print("profile form err ", profile_form.errors)
				
		# this branch handles the login logic, after a successful login
		# user is redirected to the my account page
		elif request.POST.get('submit') == 'Login':
			print("did we get here")
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				print("The login was successful")
				return redirect(reverse('hamster:my_account'))
				#add code to move them to the story selection or my account
			else:
				print(f"Invalid login details: {username}, {password}")
				return HttpResponse("Invalid login details supplied")
	else:
	# this part handles the case of not getting a POST request, i.e. the 
	# page was just loaded, thus prepare the forms to be displayed.
		user_form = UserForm()
		profile_form = UserProfileForm()
		
	return render(request, 'hamster/start.html',
					context = {'user_form':user_form,
					'profile_form': profile_form,
					'registered':registered})
					
@login_required
def my_account(request):
	if request.method == 'POST':
		# instantiate the form to update the picture
		p_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
		if p_update_form.is_valid():
			p_update_form.save()
			return redirect(reverse('hamster:my_account'))
		else:
			print(p_update_form.errors)
	else:
		# if it wasn't a POST request instantiate the form with the current user's picture
		p_update_form = ProfileUpdateForm(instance=request.user.userprofile)
	context = {'p_update_form': p_update_form,}
	return render(request, 'hamster/my_account.html', context)

@login_required
def user_logout(request):
	logout(request)
	return redirect(reverse('hamster:start'))
	
	
#helper function which parses the story's storyname variable, which is composed of the current user's attributes
def get_story_vals(title):
	values = {}
	values['story'] = title[0]
	values['day'] = title[1]
	values['hour'] = title[2:4]
	values['minutes'] = title[4:6]
	values['health'] = title[6:8]
	return values