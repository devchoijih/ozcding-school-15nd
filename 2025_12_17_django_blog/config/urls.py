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
from django.views.generic import TemplateView, RedirectView

import blog.views as views
from django.shortcuts import redirect, render
from django.urls import include, path, reverse
from django.views import View
from member import views as member_views
import blog.cb_views as cb_views

class AboutView(TemplateView):
    template_name = 'about.html'

class TestView(View):
    def get(self, request):
        return render(request, 'test_get.html')

    def post(self, request):
        return render(request, 'test_post.html')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<int:pk>/", views.blog_detail, name="blog_detail"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', member_views.sign_up, name="signup"),
    path('blog/create/', views.blog_create, name="blog_create"),
    path('blog/<int:pk>/update/', views.blog_update, name="blog_update"),
    path('blog/<int:pk>/delete/', views.blog_delete, name="blog_delete"),

    path('cb/', cb_views.BlogListView.as_view(), name='cb_blog_list'),

    path('about', AboutView.as_view(), name='about'),
    path('redirect/', RedirectView.as_view(pattern_name='about'), name='redirect'),
    path('redirect2/', lambda req: redirect(reverse('about'))),

    path('test/', TestView.as_view()),

]
