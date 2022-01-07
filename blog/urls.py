from django.urls import path
from .views import PostListView, PostUpdateView, PostDeleteView, UserPostListView, PostCreateView, UmpublishedPostListView, SearchView
from . import views as user_views

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('category/<category>/', user_views.blog_category, name="blog_category"),
    path('search/', SearchView.as_view(), name="search_results"),
    path('post/<slug:slug>/', user_views.post_detail, name="blog_detail"),
    path('user/post-status/', UmpublishedPostListView.as_view(),
         name='user-drafts'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),

]