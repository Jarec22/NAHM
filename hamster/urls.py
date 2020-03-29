from django.urls import path
from hamster import views

app_name = 'hamster'

urlpatterns = [
	path('', views.start, name='start'),
	path('about/', views.about, name='about'),
	path('logout/', views.user_logout, name='logout'),
	path('my_account/', views.my_account, name='my_account'),
	path('index/', views.index, name='index'),
	path('faq/', views.faq, name='faq'),
	path('contacts/', views.contacts, name='contacts'),
]
