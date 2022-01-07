from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Category, Post, Comment
from .forms import CommentForm, PostForm
from django.contrib import messages

from django.db.models import Count


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-created')


class UmpublishedPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/unpublished_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user, status='draft')
    

def post_detail(request, slug=None):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None


    # 
    # post_tags_ids = post.tags.values_list('id', flat=True)
    # similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    # similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]
    
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            # message after submiting form
            messages.success(request, 'comment is awaiting moderation')
            return HttpResponseRedirect(reverse_lazy('blog:blog_detail', kwargs={'slug': post.slug}))
    else:
        comment_form = CommentForm()
        

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'similar_posts': similar_posts})


def blog_category(request, category):
    posts = Post.objects.filter(categories=category).order_by('-created')
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog/blog_category.html", context)


class SearchView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    # use it in template as for loop
    context_object_name = 'search'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Post.objects.filter(title__contains=query)
          result = postresult
       else:
           result = None
       return result


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'slug', 'samplebody',
              'body', 'categories', 'image', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog_home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False