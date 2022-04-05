from django.db import models

class Topic(models.Model):
    topic_name=models.CharField(max_length=200)
    children=models.ManyToManyField("self",blank=True,null=True,symmetrical=False)
    def __str__(self):
        return "%s" % (self.topic_name)

class Question(models.Model):
    question_text=models.CharField(max_length=500)
    #media=models.FileField(null=True,blank=True)
    topics=models.ManyToManyField(Topic,related_name="topic_questions")
    def __str__(self):
        return "%s" % (self.question_text)

class Answer(models.Model):
    EXCELLENT="E"
    GOOD = "G"
    AVERAGE = "A"
    POOR = "P"
    GRADE_CHOICES=[(EXCELLENT, "excellent"), (GOOD, "good"),(AVERAGE,"average"),(POOR,"poor")]
    answer=models.CharField(max_length=1000)
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES, default=EXCELLENT)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    def __str__(self):
        return "%s: %s (%s)" % (self.question,self.answer,self.grade)