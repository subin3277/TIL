from dataclasses import field
from xml.etree.ElementTree import Comment
from django import forms
from .models import Article
from .models import Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content',)
        #fields = '__all__'
        # exclude = ('title',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = '__all__'
        exclude = ('article',)
