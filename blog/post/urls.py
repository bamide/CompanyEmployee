from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('greet', views.greet, name='greet'),
    path('money', views.money, name='money'),
    path('helloo', views.helloo, name='helloo')

]
