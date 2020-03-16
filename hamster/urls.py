from django.urls import path
from hamster import views

app_name = 'hamster'
urlpatterns = [
	path('', views.start, name='start'),
]