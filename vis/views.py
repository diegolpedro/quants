from data.models import CotizacionActual
from django.views.generic import TemplateView, ListView

class PanelView(ListView):
    model = CotizacionActual
    template_name = 'panel.html'
    queryset = CotizacionActual.objects.all()