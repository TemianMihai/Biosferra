from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from authentication.models import Account2
from post.models import PostModel
from category.models import Category
from categorie.models import Categorie
from lfcat.models import Lfcategory, Legfruccategory
# Create your views here.
def index(request):
    current_user= request.user
    post = PostModel.objects.all()
    categorie = Categorie.objects.all()
    lfcat = Lfcategory.objects.all()
    legfruc = Legfruccategory.objects.all()
    categorii = Category.objects.all()
    account2 = Account2.objects.all()
    users = User.objects.all()
    query = request.GET.get("q")
    if query:
        post = post.filter(name__contains=query)
    if request.user.is_authenticated():
        template = "home.html"
    else:
        template = "home.html"
    return render_to_response(template, {
        'user':request.user,
        'post':post,
        'users':users,
        'categorii':categorii,
        'categorie':categorie,
        'lfcat':lfcat,
        'legfruc':legfruc,
        'account2':account2,
        'current_user':current_user
    })

