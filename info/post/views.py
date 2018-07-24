from io import BytesIO

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm, CommentForm
from .forms import CreateCosForm, CreateComandaForm
from .models import PostModel, Comment, CosulMeu, AdresaDeFacturare
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from authentication.models import Account2
from user_profile.models import Profile, Mesaje
from user_profile.forms import CreateMesajeForm
from django.views.generic import View


@login_required(login_url='/login')
def create_post(request):
    current_user = request.user
    form = CreatePostForm(request.POST or None, request.FILES or None,user=current_user.account2)
    if request.method == 'POST':
        if form.is_valid():
            post = form.instance
            post.author = current_user
            form.save()
            subject = 'Creare anunt'
            message = "Anuntul dumneavoastra a fost creat. Acesta va trebui verificat de un administrator inainte ca el sa fie vizualizat pe site."
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER, current_user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            messages.success(request, 'Anuntul dumneavoastra a fost salvat. Va rugam sa asteptati cateva momente pana cand acesta va fi verificat de catre un administrator. Va multumim!')
    return render(request, "create_post.html", {
        'form': form,
        'user':request.user
    })


def get_post(request, slug):
    post = get_object_or_404(PostModel,slug=slug)
    comm_parent = Comment.objects.filter(is_parent=True).filter(post=post)
    profiles = Profile.objects.all().get(userul=post.author)
    form2 = CreateCosForm(request.POST)
    if request.method == "POST" and 'btnform1' in request.POST:
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
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
        else:
            return redirect('/login')
    if request.method == "POST" and 'btnform2' in request.POST:
        if form2.is_valid() and request.user.is_authenticated:
            cos = form2.instance
            cos.anunturi = post
            cos.cumparator = request.user
            cos.vanzator = post.author
            form2.save()
            messages.success(request, 'Produsul a fost adaugat in cos')
        else:
            return redirect('/login')
    return render(request, 'Post-page.html', {
        'posts':post ,
        'user':request.user,
        'profiles':profiles,
        'comm_parent':comm_parent,
        'form2': form2
    })


@login_required(login_url='/login')
def delete_post(request, slug):
    PostModel.objects.filter(slug=slug).delete()
    return redirect('/')


@login_required(login_url='/login')
def produsele(request):
    current_user = request.user
    cosul = CosulMeu.objects.all().filter(cumparator = current_user)
    query = request.GET.get("q")
    if query:
        cosul = cosul.filter(name__contains=query)
    return render(request, 'cosul_meu.html', {
        'user':current_user,
        'cosul':cosul
    })

@login_required(login_url='/login')
def delete_cos(request, slug):
    CosulMeu.objects.filter(slug=slug).delete()
    return redirect('/cosul-meu')

@login_required(login_url='/login')
def get_comanda(request,slug):
    current_user = request.user
    comanda = PostModel.objects.get(slug=slug)
    form = CreateComandaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and request.user.is_authenticated:
            comanda1 = form.instance
            comanda1.creator = current_user
            comanda1.posesor = comanda.author
            comanda1.postcomanda = comanda
            form.save()
            return redirect(comanda.get_finalizare_url())
        else:
            return redirect('/login')
    return render(request, 'detalii_comanda.html', {
        'user':current_user,
        'form':form
    })


@login_required(login_url='/login')
def comanda(request):
    current_user = request.user
    comenzi2 = AdresaDeFacturare.objects.all().filter(creator = current_user.account.user)
    profil = Profile.objects.all()
    query = request.GET.get("q")
    if query:
        comenzi2 = comenzi2.filter(name__contains=query)
    return render(request, 'comenzi.html',{
        'user':current_user,
        'comenzi2':comenzi2,
        'profil':profil
    })


@login_required(login_url='/login')
def delete_comanda(request, slug):
    comandar = AdresaDeFacturare.objects.filter(slug=slug).first()
    data = {
        'anunt':comandar.postcomanda.name,
        'pret': comandar.postcomanda.price,
        'cantitate':comandar.postcomanda.cantity,
        'cumparator1':comandar.nume,
        'cumparator2':comandar.prenume,
        'email':comandar.email,
        'nrdetelefon':comandar.nrdetelefon,
        'localitate':comandar.localitate,
        'judet':comandar.judet,
        'adresa': comandar.adresa,
        'vanzator1':comandar.posesor.first_name,
        'vanzator2':comandar.posesor.last_name,
        'oras':comandar.posesor.account2.city,
        'judeet':comandar.posesor.account2.state,
        'adresa2': comandar.posesor.account2.adress,
        'email2': comandar.posesor.email,
        'nrdetelefon2': comandar.posesor.account2.phonenumber,
    }
    from django.template.loader import get_template
    template_object = get_template('invoice.html')
    html = template_object.render(data)
    from StringIO import StringIO
    pdf_file = StringIO()
    from xhtml2pdf import pisa
    pisa.CreatePDF(html.encode(), pdf_file, encoding='UTF-8')
    from django.core.mail import EmailMessage
    subject="Factura comanda"
    message="Comanda dumneavoastra: %s a fost incheiata cu succes ce catre %s."
    from_email = settings.EMAIL_HOST_USER
    to_list = [settings.EMAIL_HOST_USER, comandar.email]
    mail = EmailMessage(subject, message, from_email, to_list)
    mail.attach('factura.pdf', pdf_file.getvalue(), 'application/pdf')
    mail.send()
    AdresaDeFacturare.objects.filter(slug=slug).delete()
    return redirect('/')


@login_required(login_url='/login')
def get_finalizare(request, slug):
    current_user = request.user
    comanda = PostModel.objects.get(slug=slug)
    subject = 'Efectuare comanda'
    message = "Comanda dumneavoastra a fost realizata. Aceasta va ajunge la dumneavoastra in cel mai scurt timp. Daca comanda nu a ajuns la dumneavoastra in cel mult o saptamana, va rugam sa ne contactati"
    from_email = settings.EMAIL_HOST_USER
    to_list = [settings.EMAIL_HOST_USER, current_user.email]
    send_mail(subject, message, from_email, to_list, fail_silently=True)
    return render(request, "finalizare_comanda.html", {
        'user':current_user,
        'comanda':comanda
    })

@login_required(login_url='/login')
def get_comandap(request, slug):
    current_user = request.user
    anunturi = PostModel.objects.all()
    user2 = get_object_or_404(Account2, slug=slug)
    profiles = Profile.objects.all().filter(userul=user2.user)
    comandar = AdresaDeFacturare.objects.all().filter(posesor=current_user)
    form4 = CreateMesajeForm(request.POST or None)
    if request.method == 'POST':
        if form4.is_valid() and 'btnform4' in request.POST:
            mesaj = form4.instance
            mesaj.autor = current_user
            form4.save()
            messages.success(request, 'Mesajul dumneavoastra a fost trimis')
    query = request.GET.get("q")
    if query:
        anunturi = anunturi.filter(name__contains=query)
    return render(request, 'view-profilee-comenzi.html', {
        'user': current_user,
        'anunturi': anunturi,
        'profiles': profiles,
        'form4':form4,
        'user2': user2,
        'comenzi2':comandar
    })

@login_required(login_url='/login')
def get_comandat(request, slug):
    current_user = request.user
    anunturi = PostModel.objects.all()
    user2 = get_object_or_404(Account2, slug=slug)
    profiles = Profile.objects.all().filter(userul=user2.user)
    comandar = AdresaDeFacturare.objects.all().filter(creator=current_user)
    query = request.GET.get("q")
    if query:
        anunturi = anunturi.filter(name__contains=query)
    return render(request, 'view-profilee-comenzi-t.html', {
        'user': current_user,
        'anunturi': anunturi,
        'profiles': profiles,
        'user2': user2,
        'comenzi2':comandar
    })



