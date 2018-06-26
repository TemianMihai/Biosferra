from django.shortcuts import render, redirect, render_to_response,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm, CommentForm
from .forms import CreateCosForm
from .models import PostModel, Comment, CosulMeu
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import HttpResponse

@login_required(login_url='/login')
def create_post(request):
    current_user = request.user
    form = CreatePostForm(request.POST or None, request.FILES or None,user=current_user.account2)
    if request.method == 'POST':
        if form.is_valid():
            post = form.instance
            post.author = current_user
            form.save()
            messages.success(request, 'Anuntul dumneavoastra a fost salvat. Va rugam sa asteptati cateva momente pana cand acesta va fi verificat de catre un administrator. Va multumim!')
    return render(request, "create_post.html", {
        'form': form,
        'current_user':request.user
    })



def get_post(request, slug):
    post = get_object_or_404(PostModel,slug=slug)
    comm_parent = Comment.objects.filter(is_parent=True).filter(post=post)
    form2 = CreateCosForm(request.POST)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            parent_obj = None
            try:
                parent_id = Comment.objects.get(id=int(request.POST.get("parent_id")))
            except:
                parent_id = None
            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id.id)
                if parent_qs:
                    parent_obj = parent_qs.first()
                    comment.is_parent = False
                else:
                    comment.is_parent = True
            comment.post = post
            comment.user = request.user
            comment.parent = parent_obj
            comment.save()
        if form2.is_valid():
            cos = form2.instance
            cos.anunturi = post
            cos.cumparator = request.user
            cos.vanzator = post.author
            form2.save()
            messages.success(request, 'Produsul a fost adaugat in cos')
            print cos.cumparator
            print cos.vanzator
            print cos.anunturi
    return render(request, 'Post-page.html', {
        'posts':post ,
        'user':request.user,
        'comm_parent':comm_parent,
        'form2': form2
    })



@login_required
def delete_post(request, slug):
    PostModel.objects.filter(slug=slug).delete()
    return redirect('/')



@login_required
def produsele(request):
    current_user = request.user
    cosul = CosulMeu.objects.all().filter(cumparator = current_user)
    return render(request, 'cosul_meu.html', {
        'user':current_user,
        'cosul':cosul
    })

@login_required
def comenzi(request):
    current_user = request.user
    print current_user.account2.user
    cosul = CosulMeu.objects.all().filter(vanzator = current_user.account2.user)
    return render(request, 'comenzi.html',{
        'user':current_user,
        'cosul':cosul
    })