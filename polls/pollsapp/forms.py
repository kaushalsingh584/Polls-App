from dataclasses import fields
from statistics import mode
from django import forms  
from .models import Question,Answer 


class PollAddForm(forms.ModelForm):

    choice1 = forms.CharField(label = 'Choice1',max_length=100,min_length=1,widget=forms.TextInput(attrs={'class':'form-control'}))
    choice2 = forms.CharField(label = 'Choice2',max_length=100,min_length=1,widget=forms.TextInput(attrs={'class':'form-control'}))
    choice3 = forms.CharField(label = 'Choice3',max_length=100,min_length=1,widget=forms.TextInput(attrs={'class':'form-control'}))
    choice4 = forms.CharField(label = 'Choice4',max_length=100,min_length=1,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Question
        fields  = ['question_text','choice1','choice2','choice3','choice4']
        widgets = {
                'question_text':forms.Textarea(attrs= {
                'class': 'form-control',
                'row' : 5,
                'cols': 20,

            })
        }