from .index import index

from .mision_vision_principios import MvpView
from .mensaje_direccion import MensajeDireccionView
from .logros import LogrosView
from .reconocimientos_certificaciones import RecYCertView

from .ram import RamView
from .tijuana_waterkeeper import TWaterkeeperView
from .corredores_ecologicos import CorredoresEcologicosView

from .events import Events_View

from .donativos import DonativosView
from .voluntarios import VoluntarioList

from .solicitud_voluntarios import SolicitudDeVoluntariosCreate
from .solicitudes import SolicitudDeVoluntariosList
from .solicitud_detalle import SolicitudDeVoluntariosDetail
from .solicitud_borrar import SolicitudDeVoluntariosDelete
from .solicitud_aceptar import solicitud_aceptar
from .gracias import GraciasView

from .herramientas import HerramientaList
from .registrar_herramienta import HerramientaCreate
from .borrar_herramienta import HerramientaDelete
from .editar_herramienta import HerramientaUpdate

from .libros import LibroList
from .registrar_libro import LibroCreate
from .borrar_libro import LibroDelete
from .editar_libro import LibroUpdate

from .error404 import handler404
