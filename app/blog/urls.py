from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<str:year>/<str:month>/<str:day>/<str:post>/', views.post_detail, name='post_detail'),
]