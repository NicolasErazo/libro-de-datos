from django import forms
from .models import Afiliado
from .models import Usuario

FECHA_NACIMIENTO = ['1980' ,'1981' ,'1982' ,'1983' ,'1984' ,'1985' ,'1986' ,'1987' ,'1988' ,'1989' ,'1990' ,'1991' ,'1992' ,'1993' ,'1994' ,'1995' ,'1996' ,'1997' ,'1998' ,'1999' ,'2000' ,'2001' ,'2002' ,'2003' ,'2004' ,'2005' ,'2006' ,'2007' ,'2008' ,'2009' ,'2010' ,'2011' ,'2012' ,'2013' ,'2014' ,'2015' ,'2016' ,'2017' ,'2018' ,'2019' ,'2020' ,'2021' ,'2022']
TIPO_DOCUMENTO = (("", "Abrir para seleccionar"),("Cedula Ciudadania", "Cedula Ciudadania"),("Tarjeta Identidad", "Tarjeta Identidad"),("Registro Civil", "Registro Civil"),("Cedula Extranjera", "Cedula Extranjera"))
GENERO =(("", "Abrir para seleccionar"),("M", "Masculino"),("F", "Femenino"),("O", "Otro"))
EDUCATION =(("", "Abrir para seleccionar"),("Primaria", "Primaria"),("Secundaria", "Secundaria"),("Tecnico", "Tecnico"),("Tecnologo", "Tecnologo"),("Profesional", "Profesional"),("Especialista", "Especialista"),("Otro", "Otro"))
OCUPACION =(("", "Abrir para seleccionar"),("Empleado", "Empleado"),("Desempleado", "Desempleado"),("Independiente", "Independiente"),("Estudiante", "Estudiante"),("Hogar", "Hogar"),("Otro", "Otro"))
DISCAPACIDAD =(("", "Abrir para seleccionar"),("No Aplica", "No Aplica"),("Auditiva", "Auditiva"),("Física", "Física"),("Intelectual", "Intelectual"),("Múltiple", "Múltiple"),("Visual", "Visual"),("Sordoceguera", "Sordoceguera"),("Psicosocial", "Psicosocial"),("Otro", "Otro"))
GRUPO_ETNICO =(("", "Abrir para seleccionar"),("Ninguno", "Ninguno"),("Pueblos y comunidades indígenas", "Pueblos y comunidades indígenas"),("Comunidades negras o afrocolombianas", "Comunidades negras o afrocolombianas"),("Comunidad raizal", "Comunidad raizal"),("Pueblo Rom o Gitano", "Pueblo Rom o Gitano"))
COMISION =(("", "Abrir para seleccionar"),("No Aplica", "No Aplica"),("Salud", "Salud"),("Obras", "Obras"),("Educacion", "Educacion"),("Medio Ambiente", "Medio Ambiente"),("Deportes", "Deportes"),("Derechos Humanos", "Derechos Humanos"),("Cultura", "Cultura"),("Asuntos Politicos", "Asuntos Politicos"),("Juventudes", "Juventudes"),("Niñez y Adulto Mayor", "Niñez y Adulto Mayor"),("Social", "Social"),("Organizacion y Capacitación", "Organizacion y Capacitación"),("Seguridad", "Seguridad"))
REVISION_SECRETARIAL =(("", "Abrir para seleccionar"),("No Aplica", "No Aplica"),("Datos Incompletos", "Datos Incompletos"),("Error de Identificacion", "Error de Identificacion"),("Fallecimiento", "Fallecimiento"),("Inasistencia", "Inasistencia"),("No Residente", "No Residente"),("Renovacion Delegado ASOJUNTAS", "Renovacion Delegado ASOJUNTAS"),("Retiro Voluntario", "Retiro Voluntario"),("Sancionado", "Sancionado"))
DIGNATARIO =(("", "Abrir para seleccionar"),("Si", "Si"),("No", "No"))
CARGO =(("", "Abrir para seleccionar"),("No Aplica", "No Aplica"),("Presidente", "Presidente"),("Vicepresidente", "Vicepresidente"),("Tesorero", "Tesorero"),("Secretario", "Secretario"),("Fiscal", "Fiscal"),("Fiscal Suplente", "Fiscal Suplente"),("Conciliador 1", "Conciliador 1"),("Conciliador 2", "Conciliador 2"),("Conciliador 3", "Conciliador 3"),("Comision de Trabajo de Salud", "Comision de Trabajo de Salud"),("Comision de Trabajo de Obras", "Comision de Trabajo de Obras"),("Comision de Trabajo de Medio Ambiente", "Comision de Trabajo de Medio Ambiente"),("Comision de Trabajo de Educación", "Comision de Trabajo de Educación"),("Comision de Trabajo de Deportes", "Comision de Trabajo de Deportes"),("Comision de Trabajo de Derechos Humanos", "Comision de Trabajo de Derechos Humanos"),("Comision de Trabajo de Asuntos Femeninos", "Comision de Trabajo de Asuntos Femeninos"),("Comision de Trabajo de Cultura", "Comision de Trabajo de Cultura"),("Comision de Trabajo de Junventudes", "Comision de Trabajo de Junventudes"),("Comision de Trabajo de Niñoz y Adulto Mayor", "Comision de Trabajo de Niñoz y Adulto Mayor"),("Comision de Trabajo de Deportes", "Comision de Trabajo de Deportes"),("Delegado 1 ASOJUNTAS", "Delegado 1 ASOJUNTAS"),("Delegado Suplente 1 ASOJUNTAS", "Delegado Suplente 1 ASOJUNTAS"),("Delegado 2 ASOJUNTAS", "Delegado 2 ASOJUNTAS"),("Delegado Suplente 2 ASOJUNTAS", "Delegado Suplente 2 ASOJUNTAS"),("Delegado 3 ASOJUNTAS", "Delegado 3 ASOJUNTAS"),("Delegado Suplente 3 ASOJUNTAS", "Delegado Suplente 3 ASOJUNTAS"),("Delegado 4 ASOJUNTAS", "Delegado 4 ASOJUNTAS"),("Delegado Suplente 4 ASOJUNTAS", "Delegado Suplente 4 ASOJUNTAS"),("Comisión Empresarial", "Comisión Empresarial"))

ASISTENCIA =(("", "Abrir para seleccionar"),("Ausente", "Ausente"),("Presente", "Presente"),("Con Excusa", "Con Excusa"))

class crearAfiliado(forms.ModelForm):   
    class Meta:
        
        model = Afiliado
        fields = ['nombres','tipo_documento', 'numero_documento','sexo', 'telefono', 'email', 'direccion',  'nacimiento', 'educacion', 'ocupacion', 'discapacidad', 'grupo_etnico', 'comision_trabajo', 'revision_secretarial', 'dignatario', 'cargo', 'observaciones', 'important']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_documento' : forms.Select(choices=TIPO_DOCUMENTO, attrs={'class': 'form-select'}),
            'numero_documento' : forms.NumberInput(attrs={'class': 'form-control'}),
            'sexo' : forms.Select(choices = GENERO, attrs={'class': 'form-select'}),
            'telefono' : forms.NumberInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'nacimiento' : forms.SelectDateWidget(years=FECHA_NACIMIENTO, attrs={'class': 'form-select'}),
            'educacion' : forms.Select(choices = EDUCATION, attrs={'class': 'form-select'}),
            'ocupacion' : forms.Select(choices = OCUPACION, attrs={'class': 'form-select'}),
            'discapacidad' : forms.Select(choices = DISCAPACIDAD, attrs={'class': 'form-select'}),
            'grupo_etnico' : forms.Select(choices = GRUPO_ETNICO, attrs={'class': 'form-select'}),
            'comision_trabajo' : forms.Select(choices = COMISION, attrs={'class': 'form-select'}),
            'revision_secretarial' : forms.Select(choices = REVISION_SECRETARIAL, attrs={'class': 'form-select'}),
            'dignatario' : forms.Select(choices = DIGNATARIO, attrs={'class': 'form-select'}),
            'cargo' : forms.Select(choices = CARGO, attrs={'class': 'form-select'}),
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input text-center'}),
        }
    
class crearUsuario(forms.ModelForm):   
    class Meta:
        
        model = Usuario
        fields = ['nombres','numero_documento','asistencia']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_documento' : forms.NumberInput(attrs={'class': 'form-control'}),
            'asistencia' : forms.Select(choices = ASISTENCIA, attrs={'class': 'form-select'}),
        }