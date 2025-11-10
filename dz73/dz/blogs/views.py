from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogs


def index(request):
    projects = Blogs.objects.all()
    return render(request, 'blogs/index.html', {'projects': projects})

