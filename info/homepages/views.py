from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from authentication.models import Account2
from post.forms import FilterForm
from post.models import PostModel, CHOICES_SEASON, CHOICES_UM
from category.models import Category
from categorie.models import Categorie
from lfcat.models import Products, CHOICES_TYPE


# Create your views here.
def index(request):
    current_user = request.user
    post = PostModel.objects.all()
    season = CHOICES_SEASON
    type = CHOICES_TYPE
    products = Products.objects.all()
    unity = CHOICES_UM
    seller = Account2.objects.all()
    users = User.objects.all()
    query = request.GET.get("q")
    form = FilterForm()
    if query:
        post = post.filter(name__contains=query)
    if request.user.is_authenticated():
        template = "home.html"
    else:
        template = "home.html"
    return render(request, template, {
        'user': current_user,
        'post': post,
        'users': users,
        'categorii': unity,
        'categorie': season,
        'lfcat': type,
        'legfruc': products,
        'account2': seller,
        'form': form
    })


def anotimp_legume(request, type):
    current_user = request.user
    season = CHOICES_SEASON
    seller = Account2.objects.all()
    product = Products.objects.all()
    um = CHOICES_UM
    users = User.objects.all()
    post = PostModel.objects.all().filter(season=type, product_type__type=0)
    form = FilterForm()
    return render(request, "home.html", {
        'user': current_user,
        'post': post,
        'users': users,
        'categorii': um,
        'categorie': season,
        'lfcat': CHOICES_TYPE[0],
        'legfruc': product,
        'account2': seller,
        'form': form
    })


def anotimp_fructe(request, type):
    current_user = request.user
    season = CHOICES_SEASON
    seller = Account2.objects.all()
    product = Products.objects.all()
    um = CHOICES_UM
    users = User.objects.all()
    post = PostModel.objects.all().filter(season=type, product_type__type=1)
    form = FilterForm()
    return render(request, "home.html", {
        'user': current_user,
        'post': post,
        'users': users,
        'categorii': um,
        'categorie': season,
        'lfcat': CHOICES_TYPE[1],
        'legfruc': product,
        'account2': seller,
        'form': form
    })
