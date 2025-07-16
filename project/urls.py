from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),  # all post URLs inside post/urls.py
    path('auth/', include('authentication.urls')),
]
