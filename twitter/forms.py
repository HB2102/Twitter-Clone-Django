from django import forms
from .models import Tweet


class TweetForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.Textarea(
                               attrs={
                                   'placeholder': "Write your Tweet!",
                                   'class': 'form-control',
                               }
                           ),
                           label='',
                           )

    class Meta:
        model = Tweet
        # fields = '__all__'
        exclude = ('user',)
