from django.shortcuts import render
from .models import topic
# Create your views here.
def index(request):
	return render(request,'learning_logs/index.html')

def topics(request):
	topics = topic.objects.order_by('date_added')
	context = {'topics':topics}
	return render(request , 'learning_logs/topics.html',context)