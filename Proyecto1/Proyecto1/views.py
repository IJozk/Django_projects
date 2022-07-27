from django.http import HttpResponse
import datetime

def saludo(request):

    documento="""<html>
    <body>
    <h1>
    Hola alumnos esta es nuestra primera página con Django
    </h1>
    </body>
    </html>"""

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Hasta luego alumnmos de Django.") 

def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento=f"""<html>
    <body>
    <h1>
    Fecha y hora actuales {fecha_actual}
    </h1>
    </body>
    </html>"""


    return HttpResponse(documento)

def calculaEdad(request, edad, agno):

 
    periodo=agno-2022
    edadFutura=edad+periodo

    documento=f"""<html>
    <body>
    <h1>
    En el año {agno} tendrás {edadFutura} años
    </h1>
    </body>
    </html>"""

    return HttpResponse(documento)