from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    path('select_fighter/', WarriorsSelect.as_view(), name='select_fighter'),
    path('battle/', FightView.as_view(), name='battle'),
    path('game', TemplateView.as_view(template_name='fight/battlefield.html'), name='game'),
]
