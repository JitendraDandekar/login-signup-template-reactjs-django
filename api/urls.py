from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistrationViewSet, LoginViewSet

router = DefaultRouter()
router.register('create-user', RegistrationViewSet, basename='registration')
router.register('login', LoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', LoginView.as_view())
]