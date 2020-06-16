from django import forms
from .models import Diary

class NewDiaryModelForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'content', 'image']