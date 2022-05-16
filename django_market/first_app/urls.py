from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('support/', views.support, name='sup'),
    path('login/', views.logout, name='logout'),
    path('developers/', views.developers, name='dev'),
    path('login+in/', views.signin, name='sign_in'),
    path('tin+can/', views.tin_can, name='tin_can'),
    path('dorfromantik/', views.dorfromantik, name='dorfromantik'),
    path('game', views.gapr, name='game_of_proj'),
]