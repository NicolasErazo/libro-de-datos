from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from libro.forms import crearAfiliado
from libro.models import Afiliado

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def afiliados(request):
    search = request.GET.get("buscar")
    afiliados = Afiliado.objects.filter(user=request.user, datecompleted__isnull=True)
    if search:
        afiliados = Afiliado.objects.filter(
            Q(nombres__icontains = search) |
            Q(tipo_documento__icontains = search) |
            Q(numero_documento__icontains = search) |
            Q(sexo__icontains = search) |
            Q(telefono__icontains = search) |
            Q(email__icontains = search) |
            Q(direccion__icontains = search) |
            Q(educacion__icontains = search) |
            Q(ocupacion__iexact = search) |
            Q(discapacidad__iexact = search) |
            Q(grupo_etnico__iexact = search) |
            Q(comision_trabajo__iexact = search) |
            Q(revision_secretarial__iexact = search) |
            Q(dignatario__iexact = search) |
            Q(cargo__iexact = search) |
            Q(observaciones__icontains = search) 

        )
    return render(request, 'afiliados.html', {'afiliados': afiliados})

@login_required
def afiliado_create(request):
    if request.method == 'GET':
        return render(request, 'afiliado_create.html',{
            'form': crearAfiliado
        })
    else:
        try:
            form = crearAfiliado(request.POST)
            nuevo_afiliado = form.save(commit=False)
            nuevo_afiliado.user = request.user
            nuevo_afiliado.save()
            return redirect('afiliados')
            
        except ValueError:
            return render(request, 'afiliado_create.html',{
                'form': crearAfiliado,
                'error': 'Por favor proporcione datos válidos'
            })

        except IntegrityError:
            return render(request, 'afiliado_create.html',{
                'form': crearAfiliado,
                'error': 'Por favor seleccione una fecha de nacimiento real'
            })   

@login_required
def afiliado_detail(request, afiliado_id):
    if request.method == 'GET':
        afiliado = get_object_or_404(Afiliado, pk=afiliado_id, user=request.user)
        form = crearAfiliado(instance=afiliado)
        return render(request, 'afiliado_detail.html',{'afiliado':afiliado, 'form': form})
    else:
        try:
            afiliado = get_object_or_404(Afiliado, pk=afiliado_id, user=request.user)
            form = crearAfiliado(request.POST, instance=afiliado)
            form.save()
            return redirect('afiliados')
        except ValueError:
            return  render(request, 'afiliado_detail.html',{'afiliado':afiliado, 'form': form,
            'error': 'Error actualizando Afiliado'}) 

@login_required
def afiliado_completed(request, afiliado_id):
    afiliado = get_object_or_404(Afiliado, pk=afiliado_id, user=request.user)
    if request.method == 'POST':
        afiliado.datecompleted = timezone.now()
        afiliado.save()
        return redirect('afiliados')

@login_required
def afiliados_completed(request):
    afiliados = Afiliado.objects.filter(user=request.user, datecompleted__isnull=False).order_by
    ('-datecompletedx')
    return render(request, 'afiliados.html', {'afiliados': afiliados})

@login_required
def afiliado_delete(request, afiliado_id):
    afiliado = get_object_or_404(Afiliado, pk=afiliado_id, user=request.user)
    if request.method == 'POST':
        afiliado.delete()
        return redirect('afiliados') 

@login_required
def afiliado_pdf(request, afiliado_id):
    afiliado = get_object_or_404(Afiliado, pk=afiliado_id, user=request.user)
    if request.method == 'POST':
        #Codigo PDF
        return redirect('afiliados')           

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exist'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': 'Username or Password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')
       
@login_required
def exit(request):
    logout(request)
    return redirect('home')