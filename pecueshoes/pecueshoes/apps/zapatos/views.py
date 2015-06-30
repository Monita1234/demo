# vistas de la aplicacion zapatos
from django.shortcuts import render_to_response
from django.template import RequestContext
from pecueshoes.apps.zapatos.forms import add_zapatos_form
from pecueshoes.apps.zapatos.models import Zapatos 
from django.http import HttpResponseRedirect


def add_zapatos_view(request):
	info = "inicializando"
	if request.method =="POST": #si es POST
		formulario = add_zapatos_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()#Guarda la informacion
			formulario.save_m2m()#guarda las relaciones ManyTomany
			info = "se guardo satisfactoriamete"
			return HttpResponseRedirect('/zapatos/')
	else:
		formulario = add_zapatos_form()
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('zapatos/add_zapatos.html', ctx,context_instance = RequestContext(request))
	
def edit_zapatos_view(request, id_zap):
	info = ""
	zap = Zapatos.objects.get(pk = id_zap)
	if request.method == "POST":
		formulario = add_zapatos_form(request.POST, request.FILES, instance= zap)
		if formulario.is_valid():
			edit_zap = formulario.save(commit = False)
			formulario.save_m2m()
			edit_zap.save()
			info = "Guardados satisfactoriamente"
			return HttpResponseRedirect('/zapatos/%s'% edit_zap.id)

	else:
		formulario = add_zapatos_form(instance = zap)

	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('zapatos/edit_zapatos.html', ctx,context_instance = RequestContext(request))
