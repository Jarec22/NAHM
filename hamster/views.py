from django.shortcuts import render
from django.http import HttpResponse

def start(request):
	context_dict = {'boldmessage': 'Nyarlathotep Ate My Hamster'}
	return render(request, 'hamster/start.html', context_dict)