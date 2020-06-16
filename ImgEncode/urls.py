from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from Encode import api_views
from Encode import views

router = routers.DefaultRouter()
router.register('imagedata', api_views.ImageViewSet)
router.register('custom-image', api_views.CustomImage, basename = 'Encode')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Encode.urls')),
    # path('api/', views.apiOverview, name = 'overview'),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/image-list', views.imageList, name= 'image-list'),
    # path('api/image-detail/<int:pk>', views.imageDetail, name= 'image-detail'),
    # path('api/image-create', views.imageCreate, name= 'image-create'),
    path('api/image-api', views.ImageApi.as_view(), name= 'image-api'),

]
