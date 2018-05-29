from django.urls import path
from .import views

urlpatterns = [
    path('home', views.goHomepage, name='home'),
    path('addqlandingpage', views.AddQuestionLandingPage, name='addqlandingpage'),

    path('addengqa', views.AddEnglishQuestionAnsAnswer, name='addengqa'),
    path('valqnumber', views.validate_Question_Number, name='valqnumber'),
    path('showenquestion/<enq_id>', views.ShowEngQuesion, name='showenquestion'),
    path('addfrench', views.AddFrenchQuestionAnsAnswer, name='addfrench'),
    path('addswahili',views.AddSwahiliQuesionandAnswers, name='addswahili'),
    path('addmandarin',views.AddMandarinQuestionAnsAnswers, name='addmandarin'),

    path('viewqaenglish', views.ViewEnglishQuestionAnswers, name='viewqaenglish'),
    path('viewqafrench', views.ViewFrenchQuestionAnswers, name='viewqafrench'),
    path('viewswahili', views.ViewSwahiliQuestionAnswers, name='viewswahili'),
    path('viewchinese', views.ViewMandarinQuestionAnswers, name='viewchinese'),

    path('engtest', views.TakeEnglishTest, name='engtest'),

    path('', views.index, name='index'),

    path('gradenglish', views.GradeEngish, name='gradenglish'),
    path('engscore', views.EnglishScore, name='engscore'),
    path('stdashboard', views.StudentDashboard, name='stdashboard'),
]
