from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Blogpost

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)
    print(post)
    return render(request, 'blog/blogpost.html')


def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'blog/contact.html')