from django.shortcuts import render, redirect
from form import LoginForm,UserRegisterForm,AccRegisterForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        errors = []
        form = LoginForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                user = authenticate(username = form.cleaned_data['username'],
                                    password = form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    errors.append('Incorrect username or password')
            else:
                errors.append('Form is not valid')
        return render(request, "login.html", {
            'form':form,
            'errors':errors
        })

def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    form = UserRegisterForm(data=request.POST or None)
    acc_form = AccRegisterForm(data=request.POST or None)
    errors = []
    if request.method == 'POST':
        if form.is_valid() == True and acc_form.is_valid() == True:
            form.instance.set_password(form.cleaned_data['password'])
            form.save()
            acc_form.instance.user = form.instance
            acc_form.save()
            user = authenticate(username=form.instance.username,
                                password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/')
    return render(request, "register.html", {
        'form': form,
        'acc_form' : acc_form,
        'errors': errors
    })
