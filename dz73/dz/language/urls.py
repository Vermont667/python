from django.urls import path
from . import views


urlpatterns = [
    path('', views.languages, name='languages'),
    path('<int:language_id>', views.detail, name='detail'),
]
