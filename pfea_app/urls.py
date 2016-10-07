from django.conf.urls import url

from .views import index
# or from .views.index import IndexView

app_name = 'pfea_app'
urlpatterns = [
    url(r'^$', index.IndexView.as_view(), name='index'),
]
