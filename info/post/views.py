
from django.shortcuts import render, redirect, render_to_response,get_object_or_404
from django.contrib.auth.decorators import login_required
from forms import CreatePostForm
from .models import PostModel
from django.views.decorators.http import require_POST
from django.http import HttpResponse

@login_required(login_url='/login')
def create_post(request):
    current_user = request.user
    form = CreatePostForm(request.POST or None, request.FILES or None,user=current_user)
    if request.method == 'POST':
        if form.is_valid():
            post = form.instance
            post.author = current_user
            form.save()
    return render(request, "create_post.html", {
        'form': form,
    })

def get_post(request, slug):
    post = get_object_or_404(PostModel,slug=slug)
    return render(request, 'posts/Offer-page.html', {'posts':post , 'user':request.user})