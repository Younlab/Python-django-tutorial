from django.conf.urls import url
from .views import post_list
urlpatterns = [
    # url의 첫 번째 인자: 매치될 url 정규표현식
    # url의 두 번재 인자: view function
    #   view function
    #       request를 받아서 response를 돌려주는 함수
    url(r'^$', post_list),
]

# Django 에서 처리 가능한 하나의 페이지를 만들때
# -url (특정 페이지의 URL을 설정)
# -view (URL로 들어온 request 를 처리하고 response를 돌려줄 함수)

# http://localhost:8000/^$

