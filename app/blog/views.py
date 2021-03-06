from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect

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
    # render는 주어진 1,2 번째 인수를 사용해서
    # 1번째인수 : HttpRequests 인스턴스
    # 2번째인수 : 문자열(TEMPLATE['DIRS']를 기준으로 탐색할 템플릿 파일의 경로
    # return render
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(requset, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
    }

    # post_detail view function 이 올바르게 동작하는 html을 작성해 오세요
    # post_detail.html 파일을 만들어서 post.id 값을 할당하여 해당 페이지로 넘겨주기
    return render(requset, 'blog/post_detail.html', context)


def post_create(request):
    # title
    # text
    # title = Post.objects.create(title=)
    # text = Post.objects.create(text=)
    context = {

    }
    print(request.POST.get('title'))
    print(request.POST.get('content'))
    if request.method == 'POST':
        # request의 method 값이 'POST' 일 경우
        # request.POST에 있는 title, text 값과
        # request.user 에 있는 User 인스턴스 속성을 사용해서
        # 세 post 인스턴스를 생성
        # HttpResponse를 사용해 새로생성된 인스턴스의 id, title, text 정보를 출력
        post = Post.objects.create(
            author=request.user,
            title=request.POST['title'],
            text=request.POST['content'],

        )
        # HTTP Redirection을 보낼 URL
        # http://localhost:8000/
        return redirect('post-list')
    else:
        return render(request, 'blog/post_create.html', context)


def post_delete(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.delete()
        return redirect('post-list')


def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        pass
        # 글을 수정하기
        # 1. 수정할 내용(title, text)을 가져온다
        # 2. 수정할 Post 인스턴스 명시
        # 3. 해당하는 Post 인스턴스의 title, text 를 수정해서 DB에 저장
        # 4. post_detail로 이동
        title = request.POST['title']
        text = request.POST['content']

        # 수정해서 DB에 저장
        post.title = title
        post.text = text
        post.save()
        # return HttpResponseRedirect('/{}/'.format(post_id))
        # post-detail에 해당하는 URL 을 만들어 내려면,
        # (\d+)에 해당하는 부분을 채울 값이 함께 필요
        return redirect('post-detail', post_id)
    # POST 방식이라면 어차피 위에서 return 되므로ㅓ else문 생략
    context = {
        'post':post,
    }
    return render(request, 'blog/post_edit.html', context)
