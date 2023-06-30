from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def first(request):
    if request.method=='post':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('data is submitted')
    return render(request,'first.html')
def insert(request):
    if request.method=='post':
        Topic=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=Topic)[0]
        TO.save()
        return HttpResponse('Insertion of Topic is Done')



    return render(request,'insert.html')

        
        