# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from pecueshoes.apps.home.forms import contact_form
from pecueshoes.apps.zapatos.models import Zapatos
from pecueshoes.apps.home.forms import contact_form, Login_form
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect

def index_view (request):
	return render_to_response('home/index.html',context_instance = RequestContext(request))

def about_view(request):
	mensaje = "Pecueshoes"
	ctx = {'msg': mensaje} 
	return render_to_response('home/about.html',ctx, context_instance = RequestContext(request))

def zapatos_view(request):
	zap = Zapatos.objects.all() #SELECT * FROM Producto WHERE status = True 
	ctx = {'zapatos':zap}
	return render_to_response('home/zapatos.html', ctx, context_instance = RequestContext(request))

def contacto_view(request):
	info_enviado = False #Definir si se envio la informacion o no se envio
	email = ""
	title = ""
	text = ""
	if request.method == "POST": #evalua si el metodo fue POST
		formulario = contact_form(request.POST)#instancia del formulario con los datos ingresados
		if formulario.is_valid(): #evalua si el formulario es valido
			info_enviado = True #la informacion se envio correctmente
			email = formulario.cleaned_data[ 'correo'] #copia el correo ingresado en email
			title = formulario.cleaned_data[ 'titulo'] #copia el titulo ingresado en el title
			text  = formulario.cleaned_data[ 'texto'] #copia el texto ingresado en text
			''' Bloque configuracion de envio por GMAIL '''
			to_admin = 'kaoxdc@gmail.com'
			html_content = "Iformacion recibida de %s <br>---Mensaje--- <br> %s"%(email,text)
			msg.attach_alternative(html_content,'text/html') #definimos el contenido del html
			msg.send() #enviamos el correo
			''' Fin del Bloque '''
	else: #si no fue POST entonces fue el metodo GET mostrara un formulario vacio
		formulario = contact_form() #creacion del formulario vacio
	ctx = {'form':formulario, 'email' :email, "title":title, "text":text, "info_enviado":info_enviado }
	return render_to_response ('home/contacto.html', ctx, context_instance = RequestContext(request))

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			formulario = Login_form(request.POST) 
			if formulario.is_valid():
				usu = formulario.cleaned_data['usuario']
				pas = formulario.cleaned_data['clave']
				usuario = authenticate(username = usu, password = pas)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o clave incorrecta"
		formulario = Login_form()
		ctx = {'form':formulario, 'mensaje':mensaje}
		return render_to_response('home/login.html', ctx, context_instance = RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def single_zapatos_view(request, id_zap):
	zap = Zapatos.objects.get(id = id_zap)
	ctx = {'zapatos':zap}	
	return render_to_response('home/single_zapatos.html',ctx,context_instance = RequestContext(request))
	
def administrador_view(request):
	return render_to_response('home/administrador.html'	,context_instance = RequestContext(request))
