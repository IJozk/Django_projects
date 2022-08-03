from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts  import render

class Persona(object):

    def __init__(self, nombre, apellido):

        self.nombre=nombre

        self.apellido=apellido



def saludo(request):

    p1=Persona("Jorgenitales", "Riffo")

    ahora=datetime.datetime.now()

    dia=ahora.strftime("%d")

    mes=ahora.strftime("%B")

    agno=ahora.strftime("%Y")

    temas=["Plantillas", "Modelos",
    "Formularios", "Vistas", "Despliegue"]

    ctx={"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "dia":dia, "mes":mes, "agno":agno, "temas":temas}

    # Lineas obsoletas

        # nombre="Jorge"

        # apellido="Riffo"

        #doc_externo=open("Proyecto1/plantillas/saludo.html")

        #plt=Template(doc_externo.read())

        #doc_externo.close()

        # ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "dia":dia, "mes":mes, "agno":agno, "temas":temas})

        #doc_externo=get_template('saludo.html')
        
        #documento=doc_externo.render(ctx)

    return render(request, "saludo.html", ctx)

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