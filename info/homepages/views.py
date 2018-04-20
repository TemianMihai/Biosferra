from django.shortcuts import render, render_to_response
from post.models import PostModel
from category.models import Category
# Create your views here.
def index(request):
    post = PostModel.objects.all()
    categorii = Category.objects.all()
    if request.user.is_authenticated():
        template = "home.html"
    else:
        template = "register.html"
    return render_to_response(template, {
        'user':request.user,
        'post':post,
        'categorii':categorii
    })