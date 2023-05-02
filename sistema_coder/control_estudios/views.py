from django.shortcuts import render

# Create your views here.

def listar_estudiantes(request):
    contexto = {
        "estudiantes": [
            {"nombre": "Emanuel", "apellido": "Dautel"},
            {"nombre": "Manuela", "apellido": "Gomez"},
            {"nombre": "Ivan", "apellido": "Tomasevich"},
            {"nombre": "Carlos", "apellido": "Peres"},
        ]
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_responde

    