"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render
from bookmark import views

movie_list = [
    {'title' : '파묘', 'director':'장재현'},
    {'title' : '윙카', 'director':'폴 킴'},
    {'title' : '듄', 'director':'드니 빌뇌브'},
    {'title' : '시민덕희', 'director':'박영주'}
]

def index(request):
    return HttpResponse("Hello")

def blog_list(request):

    book_text = ''

    for i in range(1, 10):
        book_text += f'book {i}<br>'

    return HttpResponse(book_text)

def book(request, num):
    book_text = f'book {num}번 페이지입니다.'
    return HttpResponse(book_text)

def language(request, lang):
    return HttpResponse(f'<h1>language: {lang} 언어 페이지입니다.')

def movies(request):
    movie_titles = [movie['title'] for movie in movie_list]
    return render(request, 'movies.html', {"movie_list":movie_list})

def movie_detail(request, movie_id):
    movie = movie_list[movie_id - 1]
    return HttpResponse(f'<h1>{movie["title"]} ({movie["director"]})</h1>')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("book_list/", blog_list),
    path("book_list/<int:num>/", book),
    path("language/<str:lang>/", language),
    path("movies/", movies),
    path("movie/<int:movie_id>", movie_detail),
    path("bookmark/", views.bookmark_list),
    path("bookmark/<int:num>", views.bookmark_detail),
]
