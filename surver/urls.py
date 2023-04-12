from django.urls import path
from . import views

app_name = 'surver'


urlpatterns = [
    path('create_surver/', views.create_surver, name='create_surver'),
    path('create_category/<int:surver_pk>/', views.create_category, name='create_category'),
    path('create_channel/<int:category_pk>/', views.create_channel, name='create_channel'),
    path('create_message/<int:channel_pk>/', views.create_message, name='create_message'),
    
    path('<int:surver_pk>/<int:channel_pk>/', views.detail, name='detail'),
    
    path('<int:surver_pk>/update/surver/', views.update_surver, name='update_surver'),
    path('<int:category_pk>/update/category/', views.update_category, name='update_category'),
    path('<int:channel_pk>/update/channel/', views.update_channel, name='update_channel'),
    path('<int:message_pk>/update/message/', views.update_message, name='update_message'),
    
    path('<int:surver_pk>/delete/surver/', views.delete_surver, name='delete_surver'),
    path('<int:category_pk>/delete/category/', views.delete_category, name='delete_category'),
    path('<int:channel_pk>/delete/channel/', views.delete_channel, name='delete_channel'),
    path('<int:message_pk>/delete/message/', views.delete_message, name='delete_message'),
    
    path('<int:message_pk>/reaction/', views.reaction, name='reaction'),
]
