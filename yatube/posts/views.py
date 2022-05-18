from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    POSTS_PER_PAGE = 10
    posts = Post.objects.select_related('group')[:POSTS_PER_PAGE]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    POSTS_PER_PAGE = 10
    group = get_object_or_404(Group, slug=slug)
    posts = (group.posting.all()[:POSTS_PER_PAGE])
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
