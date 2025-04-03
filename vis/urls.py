from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', PanelView.as_view(), name='panel'),
    path('favicon.ico', RedirectView.as_view(
         url=staticfiles_storage.url("favicon.ico"))),
    # path('data/', include('data.urls')),
    
    # path('analisis/', include('analisis.urls')),
    # path('screener-opciones/', OpcionesView.as_view(),
    #      name='screener-opciones'),
]
