from django.urls import include, path
from . import views
from rest_framework import routers
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)

app_name = 'restaurant'

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('menu/', views.MenuItemsView.as_view(), name="menu-list"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('message/', views.msg),
]   