from django.urls import path

from . import views
#from . import templates 

urlpatterns = [
    path('', views.show, name='show'),
    path('file/', views.file, name='file'),
    path('<int:question_id>/que/',views.que,name='que'),

]