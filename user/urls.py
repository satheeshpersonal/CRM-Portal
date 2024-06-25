from rest_framework import routers
from django.urls import path,include

from .views import *

app_name = 'user-data'

router = routers.DefaultRouter()
router.register('user-data', UserView,  basename='user-login')
urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view()),
]