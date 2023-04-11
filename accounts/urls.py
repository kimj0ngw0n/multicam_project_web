from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),

    path('<str:username>/', views.profile, name='profile'),
    path('<str:starname>/request_friend/', views.request_friend, name='request_friend'),
    path('<str:fanname>/accept_friend/', views.accept_friend, name='accept_friend'),

    path('<str:fanname>/delete_friend/', views.delete_friend, name='delete_friend'),
]
