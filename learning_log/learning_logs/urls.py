from django.urls import path
from . import views

app_name = 'learning_log'
urlpatterns = [
	path('',views.index,name='index'),
]