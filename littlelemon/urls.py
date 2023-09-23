
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restaurant import views 

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('restaurant/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
