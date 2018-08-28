from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from blog.forms import EmailPostForm
from blog.models import Post


def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'page':page,
        'posts':posts,
    }
    return render(request, 'post/list.html', context)

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status = 'published',
        publish__year = year,
        publish__month = month,
        publish__day = day
    )
    context = {
        'post':post,
    }
    return render(request, 'post/detail.html', context)

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} ({cd['email']}) recommends you reading {post.title}"
            message = f"Read {post.title} at {post_url} {cd['name']} {cd['comments']}"
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
        else:
            form = EmailPostForm()
        context = {
            'post':post,
            'form':form,
            'sent':sent,
        }
        return render(request, 'post/share.html', context)
