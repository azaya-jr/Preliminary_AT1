from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Deck Name')

class AuthorForm(forms.Form):
    author = forms.CharField(label='Author')

class QuestionForm(forms.Form):
    question = forms.CharField(label='Question')

class AnswerForm(forms.Form):
    answer = forms.CharField(label='Answer')
