from rest_framework import routers
from django.urls import path,include

from .views import *

app_name = 'clint-data'

router = routers.DefaultRouter()
router.register('document-data', DocumentView,  basename='user-login')
urlpatterns = [
    path('', include(router.urls)),
    path('clients/', ClientsAPIView.as_view()),
]