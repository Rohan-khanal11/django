from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,logout
from django.views.generic import CreateView, DetailView,DeleteView,ListView,UpdateView
from .models import Post  # Your Post model
from post.forms import PostForm,Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# USER = get_user_model()

# def list_post_view(request):
#     posts = Post.objects.all()
#     return render(
#         request,
#         "post/list.html",
#         context={"all_post": posts}
#     )

# def add_post_view(request):
#     context = {
#         "author": USER.objects.all()
#     }
#     return render(request, template_name="post/form.html", context=context)
class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = "post/form.html"
    form_class = PostForm
    success_url = reverse_lazy("list_post")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
class PosttDetailView(DetailView):
    model=Post
    template_name="post/details.html"

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'  # Optional, if you want confirmation page
    success_url = reverse_lazy('list_post')  
    
class ListPostView(LoginRequiredMixin, ListView):
    template_name = "post/list.html"
    context_object_name = "all_post"

    def get_queryset(self):
        current_user = self.request.user
        queryset = Post.objects.filter(author=current_user)

        query = self.request.GET.get('q','')
        if query:
            queryset = queryset.filter(author=current_user, body__icontains=query)
        else:
            queryset = queryset.filter(author=current_user)
        return queryset


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/form.html'  # Reuse the same form as create
    success_url = reverse_lazy('list_post')

    def get_queryset(self):
        # Only allow editing posts owned by the logged-in user
        return Post.objects.filter(author=self.request.user)
    

def logout_view(request):
    logout(request)
    return redirect('login')  # or wherever you want