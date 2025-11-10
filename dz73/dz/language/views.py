from django.shortcuts import render, get_object_or_404
from .models import Language


def languages(request):
    languages = Language.objects.all()
    return render(request, 'language/languages.html', {'languages': languages})


def detail(request, language_id):
    language = get_object_or_404(Language, pk=language_id)
    return render(request, 'language/details.html', {'language': language})
