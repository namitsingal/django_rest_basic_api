from django.conf.urls import patterns, url, include
from rest_framework import routers
from api.views import ItemViewSet


router = routers.DefaultRouter()
router.register(r'items',ItemViewSet)


urlpatterns = patterns(
	'',
	url(r'^', include(router.urls)),
	#url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
