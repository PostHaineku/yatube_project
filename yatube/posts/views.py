from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'posts/index.html'
    return render(request, template)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, any_slug):
    template_group_posts = 'posts/group_list.html'
    return render(request, template_group_posts)

# Create your views here.
