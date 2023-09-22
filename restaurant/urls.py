from django.urls import include, path
from . import views
from rest_framework import routers
from restaurant import views 

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]