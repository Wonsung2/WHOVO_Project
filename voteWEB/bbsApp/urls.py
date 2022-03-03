from django.contrib import admin
from django.urls    import path,include
from bbsApp         import views


urlpatterns = [
    path('index/', views.index, name = 'bbs_index'),
    path('login/', views.login, name = 'bbs_login'),
    path('joinForm/', views.joinForm, name = 'joinForm'),

]
