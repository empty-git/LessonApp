import json

from django.http import HttpResponse, FileResponse
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from Themes.models import Theme
from Themes.snippets.serializers import ThemeSerializer


# Create your views here.

def index(request):
    themes = Theme.objects.all().values('pk', 'title', 'type_lesson')
    theme_serialize = ThemeSerializer(themes,many=True)

    return HttpResponse(json.dumps(theme_serialize.data),content_type = "application/json")

def get_file(request, theme_id):
    obj = get_object_or_404(Theme, pk=theme_id)
    return FileResponse(open(obj.pdf_file.path, 'rb'), content_type='application/pdf')

def get_theme(request, theme_id):
    obj = get_object_or_404(Theme, pk=theme_id)
    return HttpResponse(obj)
