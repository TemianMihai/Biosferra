from django.shortcuts import render, render_to_response
from post.models import PostModel
# Create your views here.
def index(request):
    if request.user.is_authenticated():
        template = "home.html"
    else:
        template = "index.html"
    post = PostModel.objects.all()
    return render_to_response(template, {
        'user':request.user,
        'posts':post
    })