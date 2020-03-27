from django.shortcuts import render, redirect
from django.http import HttpResponse
from hamster.forms import UserForm, UserProfileForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def about(request):
	context_dict = {}
	print(request.method)
	print(request.user)
	return render(request, 'hamster/about.html', context=context_dict)

def start(request):
	
	registered = False
	
	if request.method == 'POST':
		# Check if the request came from the register button
		# if so handle it using the register logic and return
		# the user to the same page where they can login afterwards
		if request.POST.get('submit') == 'register':
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
		elif request.POST.get('submit') == 'login':
			print("did we get here")
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				print("The login was successful")
				return redirect('my_account')
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
			return redirect('my_account')
		else:
			print(p_update_form.errors)
	else:
		# if it wasn't a POST request instantiate the form with the current user's picture
		p_update_form = ProfileUpdateForm(instance=request.user.userprofile)
	context = {'p_update_form': p_update_form,}
	return render(request, 'hamster/my_account.html', context)