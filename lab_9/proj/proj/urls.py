"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from news import views
from news.views import ArticleCreateView
from news.views import RubricCreateView
from news.views import HashtagCreateView
from news.views import index, by_rubric

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articleCreate/', ArticleCreateView.as_view(), name='articleCreate'),
    path('rubricCreate/', RubricCreateView.as_view(), name='rubricCreate'),
    path('hashtagCreate/', HashtagCreateView.as_view(), name='hashtagCreate'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('news/', views.index),
    re_path('news/' + r'[а-яА-ЯёЁ ]+', views.rubrika),
    re_path('news/article', views.article),
    path('index/', views.index, name='index'),
]
