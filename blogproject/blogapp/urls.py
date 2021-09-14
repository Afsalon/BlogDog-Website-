from django.urls import path
from blogapp import views

urlpatterns=[
    path('',views.PostListView.as_view(), name='home_page'),
    path('draft/',views.DraftListView.as_view(), name='draft_page'),
    path('post/<int:pk>/',views.PostDetailView.as_view(), name='detail_page'),
    path('post/new/', views.PostCreateView.as_view(), name='new_page'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='update_page'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='delete_page'),
    path('post/<int:pk>/publish/',views.post_publish, name='publish_page'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='comment_page'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve_page'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove_page'),


]
