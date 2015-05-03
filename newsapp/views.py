from django.shortcuts import render
from django.http import HttpResponse
from newsapp import crawler
from newsapp import controller

#for debug
#import pdb; pdb.set_trace()

# Create your views here.

def home(request):
	return HttpResponse('Hello!')

def category(request):
	if(request.method == 'GET'):
		return HttpResponse(crawler.read_url(request.GET))

def add(reques):
	return HttpResponse(controller.add_data())