from django.template.loader import render_to_string
from django.http import HttpResponse

# Create your views here.

def post_list(request):
    html = render_to_string('blog/post_list.html')
    return HttpResponse(html)





