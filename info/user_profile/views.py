from django.shortcuts import render, redirect, get_object_or_404
from forms import Edit_profile, Edit_profile2
from authentication.models import Account2
from post.models import PostModel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
@login_required
def profile_detail(request):
    current_user = request.user
    user_form = Edit_profile(data=request.POST or None,instance=current_user,user=current_user)
    account_form = Edit_profile2(data=request.POST or None,instance=current_user.account2)
    post = PostModel.objects.filter(author=current_user)
    if request.method == 'POST':
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            return redirect('/')
    return render(request, 'edit_profile.html', {
        'form': user_form,
        'user':current_user,
        'posts':post,
        'account_form': account_form
    })




@login_required
def profile(request, slug):
    anunturi = PostModel.objects.all()
    user2 = Account2.objects.filter(slug=slug)
    if user2.count() != 0:
        return  render(request, 'view_profilee.html', {
            'user': request.user,
            'anunturi':anunturi,
            'user2':user2,
        })
    else:
        return HttpResponseForbidden()