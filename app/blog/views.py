from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

# Create your views here.
from .models import Post


def post_list(request):
    # html = render_to_string('blog/post_list.html')
    # posts = Post.objects.all()
    #
    # result = 'index<br>'
    #
    # for post in posts:
    #     result += f'-{post}<br>'
    #
    # # return HttpResponse(result)
    # return HttpResponse(result)