from .models import Question,Answer,Topic
import pandas as pd
import spacy
nlp=spacy.load("en_core_web_sm")
import sys
from django import template
register=template.Library()
@register.simple_tag
def parsing_method():
    i=0
    topic_table = pd.read_excel('Book1.xlsx',engine='openpyxl')
    df = pd.DataFrame(topic_table)
    index = df.index
    number_of_rows = len(index)
    while(i<number_of_rows):
        childs=list(map(str,topic_table['Child'].iloc[i].split(",")))
        topic,created=Topic.objects.get_or_create(topic_name=topic_table['Topicsss'].iloc[i])
        for ch in childs:
            child,created=Topic.objects.get_or_create(topic_name=ch)
            topic.children.add(child)
        quest,created=Question.objects.get_or_create(question_text=topic_table['Question'].iloc[i])
        quest.topics.add(topic)
        answers=list(map(str,topic_table['Answer'].iloc[i].split(",")))
        Grades=list(map(str,topic_table['Grade'].iloc[i].split(",")))
        for i in range(len(answers)):
            print(quest.question_text,answers[i],Grades[i])
            ans,created=Answer.objects.get_or_create(answer=answers[i],question=quest,grade=Grades[i])
            #grade,created=Answer.objects.get_or_create(grade=Grades[i])
            #ans.question.add(quest)
        i+=1

def parse(answers,transcript):
    #print(len(answers))
    for i in answers:
        doc1 = nlp(i)
        doc2 = nlp(transcript)
        print(doc1.similarity(doc2))