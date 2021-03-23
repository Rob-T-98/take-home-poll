from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from .models import Answers

class submitPageData():
    stackList = 0
    yearsList = 0
    langList = 0
    dbList = 0

class dataItem():
    key = 0
    value = 0

def createList(keys,list,numAnswers):
    newList=[]
    for key in keys:
            year = dataItem()
            num = list.count(key)
            year.key = key
            year.value = num/numAnswers*100
            newList.append(year)
        
    return newList

def convertReadable(list):
    dictionary = {'none':'None Selected',
        'pg':'PostgreSQL',
        'my':'MySQL',
        'o':'Oracle',
        'sqls':'SQL Server',
        'none':'None Selected',
        '0':'0',
        '1-2':'1-2',
        '3-4':'3-4',
        '5-6':'5-6',
        '7+':'7+',
        'none':'None Selected',
        'Front': 'Frontend',
        'Back':'Backend',
        'Both':'Both'
    }

    return [dictionary.get(item,item) for item in list]



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

        stackList = convertReadable(list(Answers.objects.values_list('stack', flat=True)))
        keys = list(dict.fromkeys(stackList))
        keys.sort()

        stackList = createList(keys,stackList,numAnswers)
        data.stackList = stackList

        langList = convertReadable(list(Answers.objects.values_list('exp', flat=True)))
        keys = list(dict.fromkeys(langList))
        keys.sort()

        langList = createList(keys,langList,numAnswers)
        data.langList = langList

        dbList = convertReadable(list(Answers.objects.values_list('db', flat=True)))
        keys = list(dict.fromkeys(dbList))
        keys.sort()

        dbList = createList(keys,dbList,numAnswers)
        data.dbList = dbList

        yearsDBList = convertReadable(list(Answers.objects.values_list('years', flat=True)))
        keys = list(dict.fromkeys(yearsDBList))
        keys.sort()

        yearsList = createList(keys,yearsDBList,numAnswers)
        
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

