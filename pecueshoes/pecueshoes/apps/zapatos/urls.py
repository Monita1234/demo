from django.conf.urls.defaults import patterns, url 

urlpatterns = patterns('pecueshoes.apps.zapatos.views',
		url (r'^add/zapatos/$','add_zapatos_view',name = 'vista_agregar_zapatos'),
		url(r'^edit/zapatos/(?P<id_zap>.*)/$','edit_zapatos_view', name= 'vista_editar_zapatos'),
	)