from django.shortcuts import render, HttpResponse

# Create your views here.
from  datetime import datetime
def hello(request):
    if request.method == 'GET':
        return HttpResponse('hello, its my first project! Enjoy! :)')

def now_date(request):
    now_time = datetime.now()
    if request.method == 'GET':
        return HttpResponse(now_time)

def goodbye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')
