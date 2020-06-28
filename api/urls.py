from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name = 'hello-viewset')
router.register('profile', views.UserProfileViewSet)
urlpatterns = [
    path('hello-api/', views.HelloApiView.as_view()),
    path('login-api/', views.UserLoginApiView.as_view()),
    path("", include(router.urls))
]