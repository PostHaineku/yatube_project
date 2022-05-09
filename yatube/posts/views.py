from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = { 'title':title }
    return render(request, template, context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, slug):
    title = 'Здесь будет информация о группах проекта Yatube'
    context = { 'title':title }
    template_group_posts = 'posts/group_list.html'
    return render(request, template_group_posts, context)

# Create your views here.
