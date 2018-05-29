from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
User = settings.AUTH_USER_MODEL
# Create your views here.JsonResponse

from .forms import QuestionandanswersForm
from .models import ProenglishQuestionsandanswers, FrenchQuestionandanswers, MandarinQuestionandanswers, SwahiliQuestionandanswers, EnglishGradiTable


@login_required
def goHomepage(request):
    return render(request, 'Protest/home.html')

def index(request):
    return render(request, 'Protest/landingpage.html')

@login_required
def AddQuestionLandingPage(request):
    return render(request, 'Protest/addqlandingpage.html')

#Add English Questions and Answers
@login_required
def AddEnglishQuestionAnsAnswer(request):
    if request.method == 'POST':
        form = QuestionandanswersForm(request.POST)
        if form.is_valid():
            newQuestion = ProenglishQuestionsandanswers.objects.create(language=request.POST['language'], section=request.POST['section'],
                          questionNumber=request.POST['questionNumber'], question=request.POST['question'],
                          AnsA=request.POST['AnsA'], AnsB=request.POST['AnsB'],AnsC=request.POST['AnsC'],AnsD=request.POST['AnsD'],
                          rightAnswer=request.POST['rightAnswer'])
            return redirect('/showenquestion/%s' % newQuestion.id)
    form = QuestionandanswersForm
    context = {'form' : form }
    return render(request, 'Protest/addenquestionandanswer.html', context)

#some Eng validation: checks if number exists.
def validate_Question_Number(request):
    questionNumber = request.GET.get('Qnumber', None)
    data = {
        'num_exist': ProenglishQuestionsandanswers.objects.filter(questionNumber__iexact=questionNumber).exists()
    }
    print(questionNumber)
    return JsonResponse(data)

@login_required
def ShowEngQuesion(request, enq_id):
    getengQuestion = ProenglishQuestionsandanswers.objects.get(pk=enq_id)
    context = {'getengQuestion' : getengQuestion}
    return render(request, 'Protest/showengqa.html', context)

@login_required
def TakeEnglishTest(request):
    getQa = ProenglishQuestionsandanswers.objects.filter(language="English", section="Grammar1")
    title = "Take English Test"
    context = {'getQa' : getQa, 'title' : title}
    return render(request, 'Protest/takeEngtest.html', context)

@login_required
def GradeEngish(request):
    if request.is_ajax and request.POST:
       #The engQID will hold questionNumber not its ID
       getSelID = request.POST.get('engQID')
       getAnsV = request.POST.get('getansValue')
    logduser = request.user.username
    logduseremail = request.user.email
    findEngQaA = ProenglishQuestionsandanswers.objects.get(questionNumber=getSelID)

    saveChoice = EnglishGradiTable(language=findEngQaA.language, section=findEngQaA.section, questionNumber=findEngQaA.questionNumber,
                 question=findEngQaA.question, AnsA=findEngQaA.AnsA, AnsB=findEngQaA.AnsB, AnsC=findEngQaA.AnsC,
                 AnsD=findEngQaA.AnsD, rightAnswer=findEngQaA.rightAnswer, selectedAns=getAnsV, userId=logduser,
                 userEmail=logduseremail)
    saveChoice.save()

    getSavedChoice = EnglishGradiTable.objects.filter(questionNumber=getSelID, userEmail=logduseremail).count()
    if getSavedChoice > 1:
        EnglishGradiTable.objects.filter(questionNumber=getSelID, userEmail=logduseremail).delete()
    saveChoice.save()
    print(saveChoice.selectedAns)
    #for testing purposes only, please delete this when done
    recountEntries = EnglishGradiTable.objects.filter(questionNumber=getSelID, userEmail=logduseremail).count()
    print(recountEntries)
    return JsonResponse(getSelID, safe=False)


def EnglishScore(request):
    title = "Take English Test"
    lang = "English"
    logduser = request.user.username
    engScore = EnglishGradiTable.objects.filter(userId=logduser).order_by('questionNumber')
    context = {'title' : title, 'engScore' : engScore, 'lang' : lang}
    return render(request, 'Protest/englishscore.html', context)

def StudentDashboard(request):
    return render(request, 'Protest/stddashboard.html')

#add French Question and abswers
@login_required
def AddFrenchQuestionAnsAnswer(request):
    if request.method == 'POST':
        form = QuestionandanswersForm(request.POST)
        if form.is_valid():
            newQuestion = FrenchQuestionandanswers(language=request.POST['language'], section=request.POST['section'],
                          questionNumber=request.POST['questionNumber'], question=request.POST['question'],
                          AnsA=request.POST['AnsA'], AnsB=request.POST['AnsB'],AnsC=request.POST['AnsC'],AnsD=request.POST['AnsD'],
                          rightAnswer=request.POST['rightAnswer'])
            newQuestion.save()
            return redirect('viewqafrench')
    form = QuestionandanswersForm
    context = {'form' : form }
    return render(request, 'Protest/addfrenchquestionandanswer.html', context)

#add Kiswahili Questions and Aswers
@login_required
def AddSwahiliQuesionandAnswers(request):
    if request.method == 'POST':
        form = QuestionandanswersForm(request.POST)
        if form.is_valid():
            newQuestion = AddSwahiliQuestionAnsAnswers(language=request.POST['language'], section=request.POST['section'],
                          questionNumber=request.POST['questionNumber'], question=request.POST['question'],
                          AnsA=request.POST['AnsA'], AnsB=request.POST['AnsB'],AnsC=request.POST['AnsC'],AnsD=request.POST['AnsD'])
            newQuestion.save()
            return redirect('viewswahili')
    form = QuestionandanswersForm
    context = {'form' : form }
    return render(request, 'Protest/addSwahiliquestionandanswer.html', context)

#Add Chinise Questions and answers
@login_required
def AddMandarinQuestionAnsAnswers(request):
    if request.method == 'POST':
        form = QuestionandanswersForm(request.POST)
        if form.is_valid():
            newQuestion = MandarinQuestionandanswers(language=request.POST['language'], section=request.POST['section'],
                          questionNumber=request.POST['questionNumber'], question=request.POST['question'],
                          AnsA=request.POST['AnsA'], AnsB=request.POST['AnsB'],AnsC=request.POST['AnsC'],AnsD=request.POST['AnsD'])
            newQuestion.save()
            return redirect('viewchinese')
    form = QuestionandanswersForm
    context = {'form' : form }
    return render(request, 'Protest/addMandarinQuestionandans.html', context)

@login_required
def ViewEnglishQuestionAnswers(request):
    getQa = ProenglishQuestionsandanswers.objects.filter(language="English")
    title = "English Questions"
    context = {'getQa' : getQa, 'title' : title}
    return render(request, 'Protest/viewQuestions.html', context)

#add func to filter questions so only french appear
@login_required
def ViewFrenchQuestionAnswers(request):
    getQa = FrenchQuestionandanswers.objects.filter(language='French')
    title = "French Questions"
    context = {'getQa' : getQa, 'title' : title}
    return render(request, 'Protest/viewQuestions.html', context)

@login_required
def ViewSwahiliQuestionAnswers(request):
    getQa = SwahiliQuestionandanswers.objects.filter(language="Swahili")
    title = "Swahili Questions"
    context = {'getQa' : getQa, 'title' : title}
    return render(request, 'Protest/viewQuestions.html', context)

@login_required
def ViewMandarinQuestionAnswers(request):
    getQa = MandarinQuestionandanswers.objects.filter(language="Mandarin")
    title = "Mandarin Questions"
    context = {'getQa' : getQa, 'title' : title}
    return render(request, 'Protest/viewQuestions.html', context)
