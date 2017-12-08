from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        template = "home.html"
    else:
        template = "index.html"
    return render_to_response(template, {
        'user':request.user
    })