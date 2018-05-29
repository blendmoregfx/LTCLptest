from django.db import models

# Create your models here.

class ProenglishQuestionsandanswers(models.Model):
    questionHead = models.TextField(max_length=4000)
    language = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    questionNumber = models.IntegerField()
    question = models.CharField(max_length=250)

    #Answers Field
    AnsA = models.CharField(max_length=200)
    AnsB = models.CharField(max_length=200)
    AnsC = models.CharField(max_length=200)
    AnsD = models.CharField(max_length=200)

    #Right Answer Field
    rightAnswer = models.CharField(max_length=200)

    def __str__(self):
        return self.question

#This table will store the question, answers, user id, email, selected answer, correct ones and grade
class EnglishGradiTable(models.Model):
    language = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    questionNumber = models.IntegerField()
    question = models.CharField(max_length=250)

    #Answers Field
    AnsA = models.CharField(max_length=200)
    AnsB = models.CharField(max_length=200)
    AnsC = models.CharField(max_length=200)
    AnsD = models.CharField(max_length=200)

    rightAnswer = models.CharField(max_length=200)
    selectedAns = models.CharField(max_length=200)

    userId = models.CharField(max_length=150)
    userEmail = models.CharField(max_length=150)




class FrenchQuestionandanswers(models.Model):
    questionHead = models.TextField(max_length=4000)
    language = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    questionNumber = models.IntegerField()
    question = models.CharField(max_length=250)

    #Answers Field
    AnsA = models.CharField(max_length=200)
    AnsB = models.CharField(max_length=200)
    AnsC = models.CharField(max_length=200)
    AnsD = models.CharField(max_length=200)

    rightAnswer = models.CharField(max_length=200)

    def __str__(self):
        return self.question

class SwahiliQuestionandanswers(models.Model):
    questionHead = models.TextField(max_length=4000)
    language = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    questionNumber = models.IntegerField()
    question = models.CharField(max_length=250)

    #Answers Field
    AnsA = models.CharField(max_length=200)
    AnsB = models.CharField(max_length=200)
    AnsC = models.CharField(max_length=200)
    AnsD = models.CharField(max_length=200)

    rightAnswer = models.CharField(max_length=200)

    def __str__(self):
        return self.question

class MandarinQuestionandanswers(models.Model):
    questionHead = models.TextField(max_length=4000)
    language = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    questionNumber = models.IntegerField()
    question = models.CharField(max_length=250)

    #Answers Field
    AnsA = models.CharField(max_length=200)
    AnsB = models.CharField(max_length=200)
    AnsC = models.CharField(max_length=200)
    AnsD = models.CharField(max_length=200)

    rightAnswer = models.CharField(max_length=200)

    def __str__(self):
        return self.question
