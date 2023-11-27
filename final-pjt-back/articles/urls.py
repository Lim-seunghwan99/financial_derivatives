from django.urls import path
from . import views
from .views import UserProfileAPIView

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('articles/<int:article_pk>/delete/', views.article_delete),
    path('articles/<int:article_pk>/comments/', views.comment_list),
    path('comments/<int:article_pk>/', views.create_comment),
    path('<article_pk>/comments/<comment_pk>/delete', views.comments_delete),
    path('profile/<str:username>/', UserProfileAPIView.as_view(), name='user-profile-api'),
]
