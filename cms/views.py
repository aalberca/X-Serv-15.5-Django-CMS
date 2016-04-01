from django.shortcuts import render

# Create your views here.

def pagina(request, identificador):

    try:
        pag = Pages.objets.get(id = int(identificador))
        respuesta = pag.page
    except Pages.DoesNotExist:
        respuesta = "No existe ese nombre con contenidos en la base de datos"
    return HttpResponse(respuesta)

def muestra_todo(request):
    lista = Pages.objets.all()
    respuesta = "<ol>"
    for pag in lista:
        respuesta += '<li><a href="' + str(pag.id) + '">' + pag.name + '</a>'
    respuesta += "</ol>"
    return HttpResponse(respuesta)
