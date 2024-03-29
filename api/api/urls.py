"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import \
    SetorViewSet,\
    FuncionariosViewSet,\
    ProdutosViewSet,\
    ChamadosViewSet,\
    TipoServicosViewSet,\
    ResolveViewSet,\
    UsadosViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'setores', SetorViewSet)
router.register(r'funcionarios', FuncionariosViewSet)
router.register(r'produtos', ProdutosViewSet)
router.register(r'chamados', ChamadosViewSet)
router.register(r'tipo-servicos', TipoServicosViewSet)
router.register(r'resolve', ResolveViewSet)
router.register(r'produtos-usados', UsadosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
