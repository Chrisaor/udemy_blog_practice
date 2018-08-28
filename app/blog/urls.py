from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<str:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<str:year>/<str:month>/<str:day>/<str:post>/', views.
         post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]