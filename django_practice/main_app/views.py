from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	dic = {'help':'go kill your self'}
	return render(request,'main_app/index.html',context=dic)
# Create your views here.
