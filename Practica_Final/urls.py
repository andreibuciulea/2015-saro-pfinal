from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Actividades.views.principal'),
    url(r'^todas$', 'Actividades.views.todo'),
    url(r'^ayuda$', 'Actividades.views.ayuda'),
    url(r'^rss$', 'Actividades.views.rss_principal'),
    url(r'^accounts/auth/$', 'Actividades.views.my_view'),
    url(r'^actualizar$', 'Actividades.views.actualizar'),
    url(r'^css/(?P<path>.*)$','django.views.static.serve',
    {'document_root': settings.STATIC_URL1}),
    url(r'^admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(.*)/rss$', 'Actividades.views.rss'),
    url(r'^(.*)$', 'Actividades.views.usuario'),
)
