from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from .models import Answers

class submitPageData():
    totalAnswers= 0 

    q1none = 0
    q1front = 0
    q1back = 0
    q1both = 0

    q2none = 0
    q20 = 0
    q212 = 0 
    q234 = 0
    q256 = 0
    q27 = 0

    q4none = 123
    q4p=123
    q4m = 567
    q4o=546
    q4s=6546

    yearsList = 0

class yearsItem():
    key = 0
    value = 0



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

        numAnswers = Answers.objects.all().count()

        data = submitPageData()
        data.totalAnswers = numAnswers
        data.q1None = Answers.objects.filter(stack='none').count()/numAnswers*100
        data.q1front = Answers.objects.filter(stack='Front').count()/numAnswers*100
        data.q1back = Answers.objects.filter(stack='Back').count()/numAnswers*100
        data.q1both = Answers.objects.filter(stack='Both').count()/numAnswers*100

        data.q2none = Answers.objects.filter(exp='none').count()/numAnswers*100
        data.q20 = Answers.objects.filter(exp='0').count()/numAnswers*100
        data.q212 = Answers.objects.filter(exp='1-2').count()/numAnswers*100
        data.q234 = Answers.objects.filter(exp='3-4').count()/numAnswers*100
        data.q256 = Answers.objects.filter(exp='5-6').count()/numAnswers*100
        data.q27 = Answers.objects.filter(exp='7+').count()/numAnswers*100

        data.q4none = Answers.objects.filter(db='none').count()/numAnswers*100
        data.q4p = Answers.objects.filter(db='pg').count()/numAnswers*100
        data.q4m = Answers.objects.filter(db='my').count()/numAnswers*100
        data.q4o = Answers.objects.filter(db='o').count()/numAnswers*100
        data.q4s = Answers.objects.filter(db='sqls').count()/numAnswers*100

        yearsDBList = list(Answers.objects.values_list('years', flat=True))
        keys = list(dict.fromkeys(yearsDBList))
        keys.sort()

        yearsList = []

        for key in keys:
            year = yearsItem()
            num = yearsDBList.count(key)
            year.key = key
            year.value = num/numAnswers*100
            yearsList.append(year)
        
        data.yearsList = yearsList

        context = {
            'input': newAnswer,
            'data':data,
        }
        template = loader.get_template('poll/submit.html')
        return HttpResponse(template.render(context, request))
def answers(request):
    answers_list = Answers.objects.all()
    template = loader.get_template('poll/answers.html')
    context = {
        'answers_list': answers_list,
    }
    return HttpResponse(template.render(context, request))

