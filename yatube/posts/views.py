from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    posts = Post.objects.select_related('author')
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).select_related('group')
    # Я попробовал через ManyToMany сделать привязку модели Group
    # к модели Post, но ничего не вышло, видимо я так и не понял
    # к какому полю нужно привязывать и окончательно запутался
    # решил оставить как было
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
