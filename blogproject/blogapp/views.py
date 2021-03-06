from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blogapp.models import Post,Comment
from blogapp.forms import PostForm,CommentForm
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class DraftListView(LoginRequiredMixin,ListView):
    login='/login/'
    model = Post
    template_name='blogapp/post_draft_list.html'
    context_object_name='posts'
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')

class PostDetailView(DetailView):
    model=Post


class PostCreateView(LoginRequiredMixin,CreateView):
    login='/login/'
    model=Post
    form_class=PostForm

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login='/login/'
    model=Post
    form_class=PostForm

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('home_page')


@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('home_page')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail_page', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blogapp/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('detail_page', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('detail_page', pk=post_pk)
