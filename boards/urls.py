from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('<int:board_pk>/commets/<int:comment_pk>/delete/', views.comments_delete, name = 'comments_delete'),
    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:board_pk>/edit/', views.edit, name='edit'), #GET(EDIT)/#POST(UPDATE)
    path('<int:board_pk>/delete/', views.delete, name='delete'),
    path('<int:board_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'), #GET(NEW)/POST(CREATE)
    path('', views.index, name='index'),
    #path('', views.jndex, name='jndex'),

]