from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('pecueshoes.apps.home.views',
		url(r'^$','index_view', name = 'vista_principal'),
		url(r'^about/$','about_view', name = 'vista_about'),
		url(r'^zapatos/$', 'zapatos_view', name = 'vista_zapatos'),
		url(r'^contacto/$', 'contacto_view', name = 'vista_contacto'),
		url(r'^login/$', 'login_view', name = 'vista_login'),
		url(r'^logout/$', 'logout_view', name = 'vista_logout'),
		url(r'^zapatos/(?P<id_zap>.*)/$', 'single_zapatos_view', name = 'vista_single_zapatos'),
		url(r'^administrador/$', 'administrador_view', name = 'vista_administrador'),
		


	)