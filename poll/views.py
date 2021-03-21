from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.views import generic
from .models import Answers

def submit(request):
    if(request.method != 'POST'):
        return redirect('/')
    else:
        stack = request.POST['question1']
        exp = request.POST['question2']
        years = request.POST['question3']
        db = request.POST['question4']
        newAnswer= Answers(stack=stack,exp = exp,years = years, db=db)
        newAnswer.save()
        return HttpResponse("Hello, world. You're at the polls index.") 
        
        
        

# Create your views here.
