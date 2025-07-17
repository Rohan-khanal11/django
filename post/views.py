from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, logout
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView, View
from .models import Post  # Your Post model
from post.forms import PostForm, Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    model = Post
    template_name = "post/details.html"

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/confirm_delete.html'   # Optional, if you want confirmation page
    success_url = reverse_lazy('list_post')  

class ListPostView(LoginRequiredMixin, ListView):
    template_name = "post/list.html"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        current_user = self.request.user
        queryset = Post.objects.filter(author=current_user)
        if query:
            queryset = queryset.filter(body__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = context.get('page_obj')

        if page_obj:
            start = (page_obj.number - 1) * page_obj.paginator.per_page + 1
            end = min(start + page_obj.paginator.per_page - 1, page_obj.paginator.count)
            total = page_obj.paginator.count
            context['page_range_msg'] = f"Showing {start} to {end} of {total} posts."
        else:
            context['page_range_msg'] = ""

        return context

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except EmptyPage:
            return redirect(f"{request.path}?page=1")



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
