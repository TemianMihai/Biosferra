from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Edit_profile, Edit_profile2, EditProfileForm, CreateMesajeForm, CreateReportForm, CreateFavoritForm, CreateProfileForm
from authentication.models import Account2
from post.models import PostModel
from .models import Favorit, Profile, Mesaje
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def profile_detail(request):
    current_user = request.user
    user_form = Edit_profile(data=request.POST or None, instance=current_user, user=current_user)
    account_form = Edit_profile2(data=request.POST or None, instance=current_user.account2)
    profile_form = EditProfileForm(data=request.POST or None, instance=current_user.profile)
    post = PostModel.objects.filter(author=current_user)
    if request.method == 'POST':
        if user_form.is_valid() and account_form.is_valid() and profile_form.is_valid() and 'btnform4' in request.POST:
            user_form.save()
            account_form.save()
            profile_form.save()
            messages.success(request, 'Profilul dumneavoastra a fost actualizat')
    return render(request, 'edit_profile.html', {
        'form': user_form,
        'user': current_user,
        'profile_form':profile_form,
        'posts': post,
        'account_form': account_form
    })

@login_required(login_url='/login')
def create_profile(request):
    current_user = request.user
    form = CreateProfileForm(request.POST or None, request.FILES or None, user=current_user.account2)
    profiles = Profile.objects.all().filter(userul=current_user)
    if len(profiles) > 0 :
        return redirect('/edit-profile')
    if request.method == 'POST':
        if form.is_valid():
            userul = current_user
            profile = form.instance
            profile.userul = current_user
            form.save()
            userul.is_active = False
            userul.save()
            subject = 'Registrare Biosferra'
            message = "Bine ati venit pe Biosferra. Un administrator va verifica accountul dumneavoastra, iar in cateva minute veti putea sa va inregistarti in cazul in care ati fost acceptat. " \
                      "Va multumim pentru intelegere. " \
                      "Mai jos puteti sa gasiti detalile despre accountul dumneavoastra: Username: %s Prenume: %s Nume: %s Numar de telefon: %s Oras: %s Judet: %s" % (
                      userul.username, userul.first_name, userul.last_name,
                      userul.account2.phonenumber, userul.account2.city, userul.account2.state)
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER, userul.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            return redirect('/')
    return render(request, 'create_profile.html', {
        'form': form,
        'user': current_user
    })


def profile(request, slug):
    current_user = request.user
    anunturi = PostModel.objects.all()
    user2 = Account2.objects.get(slug=slug)
    profiles = Profile.objects.all().filter(userul=user2.user)
    form = CreateMesajeForm(request.POST or None)
    form2 = CreateReportForm(request.POST or None)
    form3 = CreateFavoritForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and 'btnform1' in request.POST:
            if request.user.is_authenticated:
                mesaj = form.instance
                mesaj.autor = current_user
                mesaj.destinatar = user2.user
                form.save()
                messages.success(request, 'Mesajul dumneavoastra a fost trimis')
            else:
                return redirect('/login')

        if form2.is_valid() and 'btnform2' in request.POST:
            if request.user.is_authenticated:
                report = form2.instance
                report.autor = current_user
                report.destinatar = user2.user
                form2.save()
                messages.success(request, 'Reportul dumneavoastra a fost salvat cu succes')
                subject = 'Report'
                message = "Userul: %s a trimis un report catre: %s" % (form2.instance.autor, form2.instance.destinatar)
                from_email = settings.EMAIL_HOST_USER
                to_list = [settings.EMAIL_HOST_USER]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
            else:
                return redirect('/login')

        if form3.is_valid() and 'btnform3' in request.POST:
            if request.user.is_authenticated:
                favoriit = Favorit.objects.all().filter(ales=user2.user, alegator=current_user)
                if len(favoriit) > 0:
                    favoriit.delete()
                    messages.success(request, 'Acest user nu mai este in sectiunea de Favorit')
                else:
                    favorit = form3.instance
                    favorit.alegator = current_user
                    favorit.ales = user2.user
                    form3.save()
                    messages.success(request, 'Acest user a fost adaugat la Favorit')
            else:
                return redirect('/login')

    query = request.GET.get("q")
    if query:
        anunturi = anunturi.filter(name__contains=query)
    return render(request, 'view_profilee.html', {
        'user': current_user,
        'anunturi': anunturi,
        'form': form,
        'form2': form2,
        'form3': form3,
        'profiles':profiles,
        'user2': user2
    })

@login_required(login_url='/login')
def favoriti(request):
    current_user = request.user
    favoriti = Favorit.objects.all().filter(alegator = current_user)
    posturi = PostModel.objects.all()
    return render(request, 'favoriti.html', {
        'user':current_user,
        'favoriti':favoriti,
        'posturi':posturi
    })

@login_required(login_url='/login')
def mesaje(request):
    current_user = request.user
    mesaje = Mesaje.objects.all().filter(destinatar = current_user.account.user)
    return render(request, 'mesaje.html', {
        'user':current_user,
        'mesaje':mesaje
    })

@login_required(login_url='/login')
def mesaje_trimise(request):
    current_user = request.user
    mesaje = Mesaje.objects.all().filter(autor = current_user.account.user)
    return render(request, 'mesaje_trimise.html', {
        'user':current_user,
        'mesaje':mesaje
    })