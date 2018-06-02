from django.shortcuts import render, redirect, get_object_or_404
from forms import Edit_profile, Edit_profile2, CreateMesajeForm
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




def profile(request, slug):
    current_user = request.user
    anunturi = PostModel.objects.all()
    user2 = Account2.objects.get(slug=slug)
    form = CreateMesajeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            mesaj = form.instance
            mesaj.autor = current_user
            mesaj.destinatar=user2.user
            form.save()
    query = request.GET.get("q")
    if query:
        anunturi = anunturi.filter(name__contains=query)
    return  render(request, 'view_profilee.html', {
        'user': current_user,
        'anunturi':anunturi,
        'form':form,
        'user2':user2
    })
