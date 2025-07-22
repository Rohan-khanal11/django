from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView ,UpdateView
from django.views import View
from django.shortcuts import redirect
from authentication.forms import LoginForm, ProfileForm
from authentication.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.http import Http404

class LoginView(FormView):
    template_name = "auth/login_form.html"
    form_class = LoginForm
    success_url = reverse_lazy('list_post')

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Invalid username or password")
            return self.form_invalid(form)

class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('login'))

class CreateProfileView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'auth/profile_form.html'
    success_url = reverse_lazy('list_post')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        if hasattr(user, 'profile'):
            # Profile exists, add error and render form again
            form.add_error(None, "You have already created a profile.")
            return self.form_invalid(form)

        form.instance.user = user
        return super().form_valid(form)

    

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'auth/profile_form.html'
    success_url = reverse_lazy('list_post')

    def get_object(self, queryset=None):
        try:
            return self.request.user.profile
        except Profile.DoesNotExist:
            raise Http404("Profile not found")

    def dispatch(self, request, *args, **kwargs):
        # Ensure user can only edit their own profile (already ensured by get_object)
        if self.get_object().user != request.user:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)