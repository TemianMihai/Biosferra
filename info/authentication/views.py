from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from user_profile.models import Profile

from .form import LoginForm, UserRegisterForm, AccRegisterForm, AccRegisterForm2

def _login(form):
    if not form.is_valid():
        return None, ['Form is not valid']

    user = authenticate(username=form.cleaned_data['username'],
                        password=form.cleaned_data['password'])

    if not user:
        return None, ['Invalid credentials']

    return user, []


def login_view(request):
    if request.user.is_authenticated():
        return redirect('/')

    errors = []
    form = LoginForm(request.POST)

    if request.method == 'POST':
        user, form_errors = _login(form)

        if not user:
            errors = form_errors
        else:
            login(request, user)
            merchant_profile = Profile.objects.filter(user=user).first()

            if hasattr(user, 'account2') and not merchant_profile:
                return redirect('/create-profile')

            return redirect('/')

    return render(request, "login.html", {
        'form': form,
        'errors': errors
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
            subject = 'Inregistrare Biosferra'
            html_message = render_to_string('mail_template_register.html', {
                'message': 'Iti multumim ca v-ati inregistrat pe Biosferra. Mai jos puteti sa gasiti informatiile dumneavoastra',
                'username': form.instance.username,
                'prenume': form.instance.first_name,
                'nume': form.instance.last_name,
                'nrtel': acc_form.instance.phonenumber,
                'oras': acc_form.instance.city,
                'judet': acc_form.instance.state})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER, form.instance.email]
            send_mail(subject, plain_message, from_email, to_list, html_message=html_message, fail_silently=True)
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
