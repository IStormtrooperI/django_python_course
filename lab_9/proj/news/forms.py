from django.forms import ModelForm
from django import forms
from .models import Article
from .models import Rubric
from .models import Hashtag

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'keywords', 'annotation', 'rubNum')

class RubricForm(ModelForm):
    class Meta:
        model = Rubric
        fields = ('name', )

class HashtagForm(ModelForm):
    class Meta:
        model = Hashtag
        fields = ('name', 'articles')