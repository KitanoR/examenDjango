from django.conf.urls import include,url #se agrega include
from . import views

urlpatterns = [
    #url(r'^$',views.listar_eventos, name='home'), #se redirecciona a la url del blog
    url(r'^grado/nuevo/$', views.grado_nuevo, name = 'detEvento'), #se redirecciona a la url del blog

]
