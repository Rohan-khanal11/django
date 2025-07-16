from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views import View
from django.shortcuts import redirect
from authentication.forms import LoginForm


class LoginView(FormView):
    template_name = "auth/login_form.html"
    form_class = LoginForm
    success_url = reverse_lazy('list_post')  # where to go after successful login

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid username or password")
            return self.form_invalid(form)


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('login'))  
