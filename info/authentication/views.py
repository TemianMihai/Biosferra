from django.shortcuts import render, redirect
from .form import LoginForm,UserRegisterForm, AccRegisterForm, AccRegisterForm2
from django.contrib.auth import logout, authenticate, login

def login_view(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        errors = []
        form = LoginForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
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

def register_view2(request):
    form = UserRegisterForm(data=request.POST or None)
    acc_form2 = AccRegisterForm2(request.POST or None, request.FILES or None)
    errors = []
    if request.method == 'POST':
        if form.is_valid() == True and acc_form2.is_valid() == True:
            form.instance.set_password(form.cleaned_data['password'])
            form.save()
            acc_form2.instance.user = form.instance
            acc_form2.save()
            user = authenticate(username=form.instance.username,
                                password=form.cleaned_data['password'])
            user.is_active = False
            user.save()
            login(request, user)
            return redirect('/')
    return render(request, "register2.html", {
        'form': form,
        'acc_form2' : acc_form2,
        'errors': errors
    })
