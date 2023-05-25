from django import forms
from django.core.exceptions import ValidationError

from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'content')
        widgets = {
              'title': forms.TextInput(attrs={'class': 'form-control my-3'}),
              'content': forms.Textarea(attrs={'class': 'form-control my-3'}),
          }
        labels = {
           "content": "Write your thoughts here"
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise ValidationError('Title must be at least 3 characters long.')
        return title
