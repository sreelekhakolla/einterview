import csv
from pydoc_data import topics
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
import pandas as pd
from .models import Question,Answer,Topic
from .forms import QuestionForm

def file(request):
    return render(request,'file.html')
def show(request):
    if request.method == "POST":
        topics=request.POST.get('topics')
        #print(topics)
        bg=Question.objects.all().filter(topics__topic_name=topics)
        return render(request,'file.html',{'topics':bg})
    else:
        dis=Topic.objects.all()
        return render(request,'print.html',{'Topic':dis})
def que(request,question_id):
    answers=Answer.objects.filter(question__id=question_id)
    print(type(answers))
    return render(request,'web.html',{'answers':answers})
