from django.shortcuts import render, redirect
from .models import Solicitud
from .forms import SolicitudForm

def listar_solicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'canalizaciones/solicitudes.html', {'solicitudes': solicitudes})

def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_solicitudes')
    else:
        form = SolicitudForm()
    return render(request, 'canalizaciones/crear_solicitud.html', {'form': form})

