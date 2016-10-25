from django.conf.urls import url

# or from .views import index
from .views.index import IndexView
from .views.mision_vision_principios import MvpView

app_name = 'pfea_app'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^mision-vision-principios$', MvpView.as_view(), name='mvp'),
]
