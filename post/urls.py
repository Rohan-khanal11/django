from django.urls import path
from .views import CreatePostView, PosttDetailView, PostDeleteView, ListPostView, PostUpdateView

urlpatterns = [
    path('', ListPostView.as_view(), name='list_post'),  # root URL
    path('list-post/', ListPostView.as_view(), name='list_post_alt'),  # ✅ added this
    path('post-detail/<int:pk>/', PosttDetailView.as_view(), name='post_detail'),
    path('post-delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('create-post/', CreatePostView.as_view(), name='create_post'),
    path('post-update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
]
