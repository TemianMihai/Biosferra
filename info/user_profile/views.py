from django.shortcuts import render, redirect
from forms import Edit_profile, Edit_profile2
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile_detail(request):
    current_user = request.user
    user_form = Edit_profile(data=request.POST or None,instance=current_user,user=current_user)
    account_form = Edit_profile2(data=request.POST or None,instance=current_user.account)
    if request.method == 'POST':
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            return redirect('/')
        else:
            print 'sadsadsassssssss'
    return render(request, 'edit_profile.html', {
        'form': user_form,
        'account_form': account_form
    })