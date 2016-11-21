from django.conf.urls import url

# or from .views import index
from .views.index import index
from .views.mision_vision_principios import MvpView
from .views.mensaje_direccion import MensajeDireccionView
from .views.logros import LogrosView
from .views.reconocimientos_certificaciones import RecYCertView
from .views.ram import RamView
from .views.tijuana_waterkeeper import TWaterkeeperView
from .views.corredores_ecologicos import CorredoresEcologicosView
from .views.herramientas import HerramientaList
from .views.libros import LibroList
from .views.registrar_libro import LibroCreate
from .views.borrar_libro import LibroDelete
from .views.donativos import DonativosView
from .views.events import Events_View

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
    url(r'^events/$', Events_View.as_view(), name='eventos'),

    # Apoyanos
    url(r'^donativos/$', DonativosView.as_view(), name='donativos'),

    # Modelos
    url(r'^herramientas/$', HerramientaList.as_view(), name='lista_herramientas'),
    url(r'^libros/$', LibroList.as_view(), name='lista_libros'),
    url(r'^libros/registrar/$', LibroCreate.as_view(), name='registrar_libro'),
    url(r'^libros/(?P<pk>\d+)/borrar/$', LibroDelete.as_view(), name='borrar_libro'),
]
