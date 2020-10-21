from django.shortcuts import render

# Create your views here.
def index(requst):
	return render(requst,'learning_logs/index.html')