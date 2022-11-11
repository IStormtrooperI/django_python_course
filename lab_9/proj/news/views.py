from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Rubric
from .models import Article
from .models import Hashtag
from .forms import ArticleForm
from .forms import RubricForm
from .forms import HashtagForm


# Create your views here.

class ArticleCreateView(CreateView):
    template_name = 'articleCreate.html'
    form_class = ArticleForm
    success_url = '/index/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class RubricCreateView(CreateView):
    template_name = 'rubricCreate.html'
    form_class = RubricForm
    success_url = '/index/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class HashtagCreateView(CreateView):
    template_name = 'hashtagCreate.html'
    form_class = HashtagForm
    success_url = '/index/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

def by_rubric(request, rubric_id):
    articles = Article.objects.filter(rubNum=Rubric.objects.get(pk=rubric_id))
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'articles': articles, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'by_rubric.html', context)

def index(request):
    return render(request, 'index.html', {'rubrics': Rubric.objects.all()})


def rubrika(request):
    return render(request, 'rubrika.html', {})


def article(request):
    return render(request, 'article.html', {})
