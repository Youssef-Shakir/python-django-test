from django.urls import path
from . import views
from django.http import HttpResponse

app_name = 'main_app'
urlpatterns = [
	path('',views.index,name='index')
]