from django.conf.urls import url
from django.contrib.auth import views as auth_views

# or from .views import index
from .views.index import index
from .views.mision_vision_principios import MvpView
from .views.mensaje_direccion import MensajeDireccionView
from .views.logros import LogrosView
from .views.reconocimientos_certificaciones import RecYCertView
from .views.ram import RamView
from .views.tijuana_waterkeeper import TWaterkeeperView
from .views.corredores_ecologicos import CorredoresEcologicosView
from .views.events import Events_View
from .views.donativos import DonativosView
from .views.voluntarios import VoluntarioList
from .views.solicitud_voluntarios import SolicitudDeVoluntariosCreate
from .views.solicitudes import SolicitudDeVoluntariosList
from .views.solicitud_detalle import SolicitudDeVoluntariosDetail
from .views.solicitud_borrar import SolicitudDeVoluntariosDelete
from .views.solicitud_aceptar import solicitud_aceptar
from .views.gracias import GraciasView
from .views.herramientas import HerramientaList
from .views.registrar_herramienta import HerramientaCreate
from .views.borrar_herramienta import HerramientaDelete
from .views.editar_herramienta import HerramientaUpdate
from .views.libros import LibroList
from .views.registrar_libro import LibroCreate
from .views.borrar_libro import LibroDelete
from .views.editar_libro import LibroUpdate

app_name = 'pfea_app'
urlpatterns = [
    # Inicio
    url(r'^$', index, name='index'),

    # Quienes somos
    url(r'^mision-vision-principios/$', MvpView.as_view(), name='mvp'),
    url(r'^mensaje-de-la-direccion/$', MensajeDireccionView.as_view(), name='mensaje_direccion'),
    url(r'^logros/$', LogrosView.as_view(), name='logros'),
    url(r'^reconocimientos-y-certificaciones/$', RecYCertView.as_view(), name='rec_y_cert'),

    # Programas
    url(r'^ram/$', RamView.as_view(), name='ram'),
    url(r'^tijuana-waterkeeper/$', TWaterkeeperView.as_view(), name='t_waterkeeper'),
    url(r'^corredores-ecologicos-transfronterizos/$', CorredoresEcologicosView.as_view(), name='corredores'),

    # Eventos
    url(r'^eventos/$', Events_View.as_view(), name='eventos'),

    # Apoyanos
    url(r'^donativos/$', DonativosView.as_view(), name='donativos'),
    url(r'^voluntarios/$', SolicitudDeVoluntariosCreate.as_view(), name='voluntarios'),
    url(r'^gracias/$', GraciasView.as_view(), name='gracias'),

    # Voluntarios
    url(r'^voluntarios/solicitudes/$', SolicitudDeVoluntariosList.as_view(), name='solicitudes'),
    url(r'^voluntarios/lista/$', VoluntarioList.as_view(), name='lista_voluntarios'),
    url(r'^voluntarios/solicitudes/(?P<pk>\d+)/$', SolicitudDeVoluntariosDetail.as_view(), name='solicitud'),
    url(r'^voluntarios/solicitudes/(?P<pk>\d+)/borrar/$', SolicitudDeVoluntariosDelete.as_view(), name='borrar_solicitud'),
    url(r'^voluntarios/solicitudes/(?P<pk>\d+)/aceptar/$', solicitud_aceptar, name='aceptar_solicitud'),

    # Herramientas
    url(r'^herramientas/$', HerramientaList.as_view(), name='lista_herramientas'),
    url(r'^herramientas/registrar/$', HerramientaCreate.as_view(), name='registrar_herramienta'),
    url(r'^herramientas/(?P<pk>\d+)/borrar/$', HerramientaDelete.as_view(), name='borrar_herramienta'),
    url(r'^herramientas/(?P<pk>\d+)/editar/$', HerramientaUpdate.as_view(), name='editar_herramienta'),

    # Libros
    url(r'^libros/$', LibroList.as_view(), name='lista_libros'),
    url(r'^libros/registrar/$', LibroCreate.as_view(), name='registrar_libro'),
    url(r'^libros/(?P<pk>\d+)/borrar/$', LibroDelete.as_view(), name='borrar_libro'),
    url(r'^libros/(?P<pk>\d+)/editar/$', LibroUpdate.as_view(), name='editar_libro'),

    # Autenticacion
    url(r'^login/$', auth_views.login, { 'template_name' : 'auth/login.html' }, name='login'),
    url(r'logout/$', auth_views.logout_then_login, name='logout'),
]
