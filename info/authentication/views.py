from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
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
    form = UserRegisterForm(request.POST or None)
    acc_form = AccRegisterForm(request.POST or None)
    errors = []
    if request.method == 'POST':
        if form.is_valid() and acc_form.is_valid():
            form.instance.set_password(form.cleaned_data['password'])
            form.save()
            acc_form.instance.user = form.instance
            acc_form.save()
            subject = 'Registrare Biosferra'
            message = "Iti multumim ca v-ati inregistrat pe Biosferra. Mai jos puteti sa gasiti informatiile dumneavoastra:Username: %s Prenume: %s Nume: %s Numar de telefon: %s Oras: %s Judet: %s" %(form.instance.username, form.instance.first_name, form.instance.last_name, acc_form.instance.phonenumber, acc_form.instance.city, acc_form.instance.state)
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER, form.instance.email]

            send_mail(subject,message,from_email,to_list,fail_silently=True)

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
        if form.is_valid() and acc_form2.is_valid():
            form.instance.set_password(form.cleaned_data['password'])
            form.save()
            acc_form2.instance.user = form.instance
            acc_form2.save()
            user = authenticate(username=form.instance.username,
                                password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/create-profile')
    return render(request, "register2.html", {
        'form': form,
        'acc_form2': acc_form2,
        'errors': errors
    })
