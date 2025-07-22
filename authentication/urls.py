from django.urls import path
from authentication.views import LoginView, LogoutView, CreateProfileView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("create-profile/", CreateProfileView.as_view(), name="create_profile"),
]
