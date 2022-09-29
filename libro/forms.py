from django import forms
from .models import Afiliado

FECHA_NACIMIENTO = ['1980' ,'1981' ,'1982' ,'1983' ,'1984' ,'1985' ,'1986' ,'1987' ,'1988' ,'1989' ,'1990' ,'1991' ,'1992' ,'1993' ,'1994' ,'1995' ,'1996' ,'1997' ,'1998' ,'1999' ,'2000' ,'2001' ,'2002' ,'2003' ,'2004' ,'2005' ,'2006' ,'2007' ,'2008' ,'2009' ,'2010' ,'2011' ,'2012' ,'2013' ,'2014' ,'2015' ,'2016' ,'2017' ,'2018' ,'2019' ,'2020' ,'2021' ,'2022']
TIPO_DOCUMENTO = (("", "Abrir para seleccionar"),("Cedula Ciudadania", "Cedula Ciudadania"),("Tarjeta Identidad", "Tarjeta Identidad"),("Registro Civil", "Registro Civil"),("Cedula Extranjera", "Cedula Extranjera"))
GENERO =(("", "Abrir para seleccionar"),("M", "Masculino"),("F", "Femenino"),("O", "Otro"))
EDUCATION =(("", "Abrir para seleccionar"),("Primaria", "Primaria"),("Secundaria", "Secundaria"),("Tecnico", "Tecnico"),("Tecnologo", "Tecnologo"),("Profesional", "Profesional"),("Especialista", "Especialista"))
OCUPACION =(("", "Abrir para seleccionar"),("Empleado", "Empleado"),("Desempleado", "Desempleado"),("Independiente", "Independiente"),("Estudiante", "Estudiante"))
DISCAPACIDAD =(("", "Abrir para seleccionar"),("Ninguna", "Ninguna"))
GRUPO_ETNICO =(("", "Abrir para seleccionar"),("Ninguna", "Ninguna"))
COMISION =(("", "Abrir para seleccionar"),("Ninguna", "Ninguna"))

class crearAfiliado(forms.ModelForm):
    class Meta:
        
        model = Afiliado
        fields = ['nombres','tipo_documento', 'numero_documento','sexo', 'telefono', 'email', 'direccion',  'nacimiento', 'educacion', 'ocupacion', 'discapacidad', 'grupo_etnico', 'comision_trabajo', 'observaciones', 'important']
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
            'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input text-center'}),
        }
    
