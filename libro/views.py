from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from fpdf import FPDF
from django.http import HttpResponse
from datetime import datetime

from libro.forms import crearAfiliado
from libro.pdf import PDFTable, PDF
from libro.models import Afiliado
from libro.forms import crearUsuario
from libro.models import Usuario


@login_required
def afiliado_pdf(request, afiliado_id):

    afiliados = get_object_or_404(Afiliado, pk=afiliado_id, user=request.user)
    NombreMayus = afiliados.nombres.upper()
    now = datetime.now()

    if request.method == 'POST':

        pdf = PDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.multi_cell(
            0, 10, f'La Junta De Accion Comunal BARRIO PABLO SEXTO del municipio de Acacias - Meta, a solicitud del interesado informa que el(la) Señor(a) {NombreMayus}, identificado(a) con la {afiliados.tipo_documento} número {afiliados.numero_documento} está afiliado(a) a esta Organización de Acción Comunal desde el {afiliados.created.year}-{afiliados.created.month}-{afiliados.created.day}, en el folio 2 con el número de registro 2 del libro de afiliados.', 0, 'J')
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.multi_cell(
            0, 10, f'Se expide en el municipio de Acacias el día {now.day} de {now.month} de {now.year}. Puede verificar la autenticidad de este documento ingresando a la pagina web https://librodigital.onrender.com en la seccion de edición de Afiliados', 0, 'J')
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.set_font('Arial', 'B', 12)
        pdf.multi_cell(
            0, 10, '______________________________         ______________________________', 0, 'C')
        pdf.multi_cell(
            0, 10, 'ANSELMO QUEVEDO                                 CLAUDIA PATRICIA PAEZ', 0, 'C')
        pdf.multi_cell(
            0, 10, 'PRESIDENTE(A)                                           SECRETARIO(A)', 0, 'C')

        response = HttpResponse(pdf.output(dest='S').encode(
            'latin-1'), content_type='application/pdf')
        response['Content-Disposition'] = f"attachment; filename=Afiliado_{afiliados.nombres}.pdf"
        return response


def home(request):
    return render(request, 'home.html')


@login_required
def afiliados(request):
    search = request.GET.get("buscar")
    afiliados = Afiliado.objects.filter(
        user=request.user, datecompleted__isnull=True)
    if search:
        afiliados = Afiliado.objects.filter(
            Q(nombres__icontains=search) |
            Q(tipo_documento__icontains=search) |
            Q(numero_documento__icontains=search) |
            Q(sexo__icontains=search) |
            Q(telefono__icontains=search) |
            Q(email__icontains=search) |
            Q(direccion__icontains=search) |
            Q(educacion__icontains=search) |
            Q(ocupacion__iexact=search) |
            Q(discapacidad__iexact=search) |
            Q(grupo_etnico__iexact=search) |
            Q(comision_trabajo__iexact=search) |
            Q(revision_secretarial__iexact=search) |
            Q(dignatario__iexact=search) |
            Q(cargo__iexact=search) |
            Q(observaciones__icontains=search)

        )
    return render(request, 'afiliados.html', {'afiliados': afiliados})


@login_required
def asistencia(request):
    usuarios = Usuario.objects.all()
    return render(request, 'asistencia.html', {'usuarios': usuarios})


@login_required
def usuario_create(request):
    if request.method == 'GET':
        return render(request, 'usuario_create.html', {
            'form': crearUsuario
        })
    else:
        try:
            print(request.POST)
            form = crearUsuario(request.POST)
            nuevo_usuario = form.save(commit=False)
            nuevo_usuario.user = request.user
            nuevo_usuario.save()
            return redirect('asistencia')

        except ValueError:
            return render(request, 'usuario_create.html', {
                'form': crearUsuario,
                'error': 'Por favor proporcione datos válidos'
            })

        except IntegrityError:
            return render(request, 'usuario_create.html', {
                'form': crearUsuario,
                'error': 'Por favor seleccione una fecha de nacimiento real'
            })


@login_required
def afiliado_create(request):
    if request.method == 'GET':
        return render(request, 'afiliado_create.html', {
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
            return render(request, 'afiliado_create.html', {
                'form': crearAfiliado,
                'error': 'Por favor proporcione datos válidos'
            })

        except IntegrityError:
            return render(request, 'afiliado_create.html', {
                'form': crearAfiliado,
                'error': 'Por favor seleccione una fecha de nacimiento real'
            })


@login_required
def usuario_delete(request, afiliado_id):
    usuario = get_object_or_404(Usuario, pk=afiliado_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('asistencia')


@login_required
def all_delete(request):

    if request.method == 'GET':
        now = datetime.now()
        usuarios = Usuario.objects.all()
        data = [['Nombres y Apellidos',
                 'Documento de Identidad', 'Asistencia Asamblea']]

        for usuario in usuarios:
            data.append(
                [usuario.nombres, usuario.numero_documento, usuario.asistencia])

        print(data)
        pdf = PDFTable()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.set_font('Times', '', 10.0)
        epw = pdf.w - 2*pdf.l_margin
        col_width = epw/3
        th = pdf.font_size
        pdf.ln(4*th)
        pdf.cell(epw, 0.0, '', align='C')
        pdf.set_font('Times', '', 14.0)
        pdf.ln(0.5)

        for row in data:
            for datum in row:
                # Enter data in colums
                pdf.cell(col_width, 2*th, str(datum), border=1, align='C')

            pdf.ln(2*th)
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.multi_cell(0, 10, '', 0, 'J')
        pdf.set_font('Arial', 'B', 12)
        pdf.multi_cell(
            0, 10, '______________________________         ______________________________', 0, 'C')
        pdf.multi_cell(
            0, 10, 'ANSELMO QUEVEDO                                 CLAUDIA PATRICIA PAEZ', 0, 'C')
        pdf.multi_cell(
            0, 10, 'PRESIDENTE(A)                                           SECRETARIO(A)', 0, 'C')    

        response = HttpResponse(pdf.output(dest='S').encode(
            'latin-1'), content_type='application/pdf')
        response['Content-Disposition'] = f"attachment; filename=Asistencia_{now.day}/{now.month}/{now.year}.pdf"
        usuarios.delete()
        return response


@login_required
def afiliado_detail(request, afiliado_id):
    if request.method == 'GET':
        afiliado = get_object_or_404(
            Afiliado, pk=afiliado_id, user=request.user)
        form = crearAfiliado(instance=afiliado)
        return render(request, 'afiliado_detail.html', {'afiliado': afiliado, 'form': form})
    else:
        try:
            afiliado = get_object_or_404(
                Afiliado, pk=afiliado_id, user=request.user)
            form = crearAfiliado(request.POST, instance=afiliado)
            form.save()
            return redirect('afiliados')
        except ValueError:
            return render(request, 'afiliado_detail.html', {'afiliado': afiliado, 'form': form,
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
    afiliados = Afiliado.objects.filter(
        user=request.user, datecompleted__isnull=False).order_by
    ('-datecompletedx')
    return render(request, 'afiliados.html', {'afiliados': afiliados})


@login_required
def afiliado_delete(request, afiliado_id):
    afiliado = get_object_or_404(Afiliado, pk=afiliado_id, user=request.user)
    if request.method == 'POST':
        afiliado.delete()
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
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña Incorrectos'
            })
        else:
            login(request, user)
            return redirect('home')


@login_required
def exit(request):
    logout(request)
    return redirect('home')
