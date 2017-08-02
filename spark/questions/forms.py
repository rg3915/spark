from django import forms

from spark.questions.models import Answer, Question


class QuestionForm(forms.ModelForm):
    title = forms.CharField(
        label='Título',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255)
    description = forms.CharField(
        label='Descrição',
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        max_length=2000)
    tags = forms.CharField(
        label='Marcadores',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255,
        required=False,
        help_text='Use espaço para separar os marcadores, ou seja "python data science machine learning"')  # noqa: E501

    class Meta:
        model = Question
        fields = ['title', 'description', 'tags']


class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                      queryset=Question.objects.all())
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        max_length=2000)

    class Meta:
        model = Answer
        fields = ['question', 'description']