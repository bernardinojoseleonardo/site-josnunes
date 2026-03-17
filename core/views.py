from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Servico, Foto, Contacto
from .forms import ContactoForm

def home(request):
    servicos_destaque = Servico.objects.all()[:3]
    fotos_destaque = Foto.objects.filter(visivel=True, destaque=True)[:6]
    return render(request, 'home.html', {
        'servicos_destaque': servicos_destaque,
        'fotos_destaque': fotos_destaque
    })

def servicos(request):
    grafica = Servico.objects.filter(categoria='grafica')
    textil = Servico.objects.filter(categoria='textil')
    return render(request, 'servicos.html', {
        'grafica': grafica,
        'textil': textil
    })

def galeria(request):
    fotos_list = Foto.objects.filter(visivel=True)
    paginator = Paginator(fotos_list, 12)
    page_number = request.GET.get('page')
    fotos = paginator.get_page(page_number)
    return render(request, 'galeria.html', {'fotos': fotos})

def sobre(request):
    return render(request, 'sobre.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua mensagem foi enviada com sucesso! Entraremos em contacto em breve.')
            return redirect('contacto')
        else:
            messages.error(request, 'Houve um erro ao enviar sua mensagem. Por favor, verifique os campos.')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})
