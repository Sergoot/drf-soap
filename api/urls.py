from django.urls import path
from . import views
urlpatterns = [
    path('methods', views.MethodAPIView.as_view(), name='methods_list'),
    path('methods/<str:method>', views.MethodDetailAPIView.as_view(), name='method_detail')
]
