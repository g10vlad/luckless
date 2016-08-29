from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter


from .views import InvestigacionViewSet


# from .api_views import load_menu

#router = ExtendedSimpleRouter()
router = routers.DefaultRouter()

router.register(r'investigacion',  InvestigacionViewSet)

InvestigacionRouterList = InvestigacionViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

InvestigacionRouterDetail = InvestigacionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [

    url(r'^investigaci/$', InvestigacionRouterList),

    url(r'^investigaci/(?P<pk>[0-9]+)/$', InvestigacionRouterDetail),

    url(r'^', include(router.urls)),
]
