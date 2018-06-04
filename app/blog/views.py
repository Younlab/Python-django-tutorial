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
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    # render는 주어진 1,2 번째 인수를 사용해서
    # 1번째인수 : HttpRequests 인스턴스
    # 2번째인수 : 문자열(TEMPLATE['DIRS']를 기준으로 탐색할 템플릿 파일의 경로
    # return render
    return render(request, 'blog/post_list.html', context)