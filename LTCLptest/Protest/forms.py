from django import forms

class QuestionandanswersForm(forms.Form):
    language = forms.CharField(max_length=100, required=True)
    section = forms.CharField(max_length=100, required=True)
    questionNumber = forms.IntegerField(required=True)
    question = forms.CharField(max_length=250, required=True)

    #Answers Field
    AnsA = forms.CharField(max_length=200, required=True)
    AnsB = forms.CharField(max_length=200, required=True)
    AnsC = forms.CharField(max_length=200, required=True)
    AnsD = forms.CharField(max_length=200, required=True)

    #right ans Field
    rightAnswer = forms.CharField(max_length=200,required=True)
