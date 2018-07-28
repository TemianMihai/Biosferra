from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import Edit_profile, Edit_profile2, EditProfileForm, Edit_profile_buyer, CreateMesajeForm, CreateReportForm, CreateFavoritForm, CreateProfileForm
from authentication.models import Account2, Account
from django.contrib.auth.models import User
from post.models import PostModel, AdresaDeFacturare
from .models import Favourite, Profile, Message
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
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


def profile_detail2(request):
    current_user = request.user
    user_form = Edit_profile(data=request.POST or None, instance=current_user, user=current_user)
    account_form = Edit_profile_buyer(data=request.POST or None, instance=current_user.account)
    if request.method == 'POST':
        if user_form.is_valid() and account_form.is_valid() and 'btnform4' in request.POST:
            user_form.save()
            account_form.save()
            messages.success(request, 'Profilul dumneavoastra a fost actualizat')
    return render(request, 'edit_profile_buyer.html', {
        'form': user_form,
        'user': current_user,
        'account_form': account_form
    })


@login_required(login_url='/login')
def create_profile(request):
    current_user = request.user
    form = CreateProfileForm(request.POST or None, request.FILES or None, user=current_user.account2)
    profiles = Profile.objects.all().filter(user=current_user)
    if len(profiles) > 0:
        return redirect('/edit-profile')
    if request.method == 'POST':
        if form.is_valid():
            user = current_user
            profile = form.instance
            profile.user = current_user
            form.save()
            user.is_active = False
            user.save()
            subject = 'Inregistrare Biosferra'
            html_message = render_to_string('mail_template_register.html', {
                'message': 'Bine ati venit pe Biosferra. Un administrator va verifica accountul dumneavoastra, iar in cateva minute veti putea sa va inregistarti in cazul in care ati fost acceptat.',
                'message2': 'Mai jos puteti sa gasiti detalile despre accountul dumneavoastra:',
                'username': user.username,
                'prenume': user.first_name,
                'nume': user.last_name,
                'nrtel':user.account2.phonenumber,
                'oras':user.account2.city,
                'judet':user.account2.state})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER, user.email]
            send_mail(subject, plain_message, from_email, to_list, html_message=html_message, fail_silently=True)
            return redirect('/create-profile/finalizare')
    return render(request, 'create_profile.html', {
        'form': form,
        'user': current_user
    })

def mesaj_profile(request, slug):
    current_user = request.user
    useru = get_object_or_404(Account,slug=slug)
    form = CreateMesajeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            mesaj = form.instance
            mesaj.author = current_user
            mesaj.receiver = useru.user
            form.save()
            messages.success(request, 'Mesajul dumneavoastra a fost trimis')
    return render(request, "mesaj_useri.html", {
        'useru':useru,
        'user':current_user,
        'form':form
    })

def profile2(request):
    current_user = request.user
    user2 = Account.objects.get(user = current_user.account)
    return render(request, 'profile_account.html',{
        'user':current_user,
        'user2':user2
    })

def profile(request, slug):
    current_user = request.user
    posts = PostModel.objects.all()
    user2 = get_object_or_404(Account2,slug=slug)
    mesaje = Message.objects.all().filter(receiver=user2.user)
    profiles = Profile.objects.all().filter(user=user2.user)
    favoritt = Favourite.objects.all().filter(receiver=user2.user)
    messageform = CreateMesajeForm(request.POST or None)
    reportform = CreateReportForm(request.POST or None)
    favouriteform = CreateFavoritForm(request.POST or None)
    if request.method == 'POST':
        if messageform.is_valid() and 'btnform1' in request.POST:
            if request.user.is_authenticated:
                mesaj = messageform.instance
                mesaj.author = current_user
                mesaj.receiver = user2.user
                messageform.save()
                messages.success(request, 'Mesajul dumneavoastra a fost trimis')
            else:
                return redirect('/login')

        if reportform.is_valid() and 'btnform2' in request.POST:
            if request.user.is_authenticated:
                report = reportform.instance
                report.author = current_user
                report.receiver = user2.user
                reportform.save()
                messages.success(request, 'Reportul dumneavoastra a fost salvat cu succes')
                subject = 'Report'
                html_message = render_to_string('mail_template.html', {'message': 'Userul %s a trimis un report catre %s' % (report.author, report.receiver)})
                plain_message = strip_tags(html_message)
                from_email = settings.EMAIL_HOST_USER
                to_list = [settings.EMAIL_HOST_USER]
                send_mail(subject, plain_message, from_email, to_list, html_message=html_message, fail_silently=True)
            else:
                return redirect('/login')

        if favouriteform.is_valid() and 'btnform3' in request.POST:
            if request.user.is_authenticated:
                favoriit = Favourite.objects.all().filter(receiver=user2.user, author=current_user)
                if len(favoriit) > 0:
                    favoriit.delete()
                    messages.success(request, 'Acest user nu mai este in sectiunea de Favourite')
                else:
                    favorit = favouriteform.instance
                    favorit.author = current_user
                    favorit.receiver = user2.user
                    favouriteform.save()
                    messages.success(request, 'Acest user a fost adaugat la Favourite')
            else:
                return redirect('/login')
    query = request.GET.get("q")
    if query:
        posts = posts.filter(name__contains=query)
    return render(request, 'view_profilee.html', {
        'user': current_user,
        'anunturi': posts,
        'mesaje':mesaje,
        'form': messageform,
        'form2': reportform,
        'form3': favouriteform,
        'profiles':profiles,
        'favoritt':favoritt,
        'user2': user2
    })

@login_required(login_url='/login')
def favoriti(request):
    current_user = request.user
    favoriti = Favourite.objects.all().filter(author = current_user)
    posturi = PostModel.objects.all()
    query = request.GET.get("q")
    if query:
        posturi = posturi.filter(name__contains=query)
    return render(request, 'favoriti.html', {
        'user':current_user,
        'favoriti':favoriti,
        'posturi':posturi
    })

@login_required(login_url='/login')
def mesaje(request):
    current_user = request.user
    mesaje = Message.objects.all().filter(receiver = current_user.account.user)
    return render(request, 'mesaje.html', {
        'user':current_user,
        'mesaje':mesaje
    })

@login_required(login_url='/login')
def mesaje_trimise(request):
    current_user = request.user
    mesaje = Message.objects.all().filter(author = current_user.account.user)
    return render(request, 'mesaje_trimise.html', {
        'user':current_user,
        'mesaje':mesaje
    })


@login_required(login_url='/login')
def get_mesajet(request, slug):
    current_user = request.user
    anunturi = PostModel.objects.all()
    user2 = get_object_or_404(Account2,slug=slug)
    form4 = CreateMesajeForm(request.POST or None)
    favoritt = Favourite.objects.all().filter(receiver = user2.user)
    profiles = Profile.objects.all().filter(user=user2.user)
    mesaje = Message.objects.all().filter(author=current_user)
    if request.method == 'POST':
        if form4.is_valid() and 'btnform4' in request.POST:
            mesaj = form4.instance
            mesaj.author = current_user
            mesaj.receiver = mesaje.receiver
            form4.save()
            messages.success(request, 'Mesajul dumneavoastra a fost trimis')
    query = request.GET.get("q")
    if query:
        anunturi = anunturi.filter(name__contains=query)
    return render(request,'view-profilee-mesaje-t.html', {
        'user': current_user,
        'anunturi': anunturi,
        'profiles': profiles,
        'favoritt':favoritt,
        'form4':form4,
        'user2': user2,
        'mesaje':mesaje
    })

def get_profilf(request):
    return render(request, "finalizare_profil.html")

