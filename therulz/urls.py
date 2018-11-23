# -*- coding: utf-8 -*-
# @Author: Charlie Gallentine
# @Date:   2018-06-10 18:45:33
# @Last Modified by:   Charlie Gallentine
# @Last Modified time: 2018-06-12 21:32:43

from django.urls import path

from . import views

app_name = 'therulz'
urlpatterns = [
	path('', views.IndexView.as_view(), name='IndexView'),
	path('about/', views.about, name='about'),
	path('search/', views.search, name='search'),
	path('<int:game_id>/', views.game, name='game'),
]