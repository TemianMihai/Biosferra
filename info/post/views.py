
from django.shortcuts import render, redirect, render_to_response,get_object_or_404
from django.contrib.auth.decorators import login_required
from forms import CreatePostForm, CommentForm
from .models import PostModel, Comment
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
            return redirect('/')
    return render(request, "create_post.html", {
        'form': form,
        'current_user':request.user
    })



def get_post(request, slug):
    post = get_object_or_404(PostModel,slug=slug)
    comm_parent = Comment.objects.filter(is_parent=True).filter(post=post)
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
    return render(request, 'Post-page.html', {'posts':post , 'user':request.user, 'comm_parent':comm_parent})



@login_required
def delete_post(request, slug):
    PostModel.objects.filter(slug=slug).delete()
    return redirect('/')
