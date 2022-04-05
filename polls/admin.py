from django.contrib import admin
from . models import Topic,Question,Answer
#from import_export.admin import ImportExportModelAdmin
admin.site.register(Topic)
admin.site.register(Answer)
class AnswerInline(admin.TabularInline):
   model = Answer
class QuestionAdmin(admin.ModelAdmin):
   model=Question
   inlines = [AnswerInline,]
admin.site.register(Question, QuestionAdmin)
