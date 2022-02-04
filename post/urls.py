from django.urls import path, include
import post.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('post/<int:post_id>/', views.post_details, name='post'),
    path('author/<int:author_id>/', views.author_view, name='author'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration, name='registration'),
]
