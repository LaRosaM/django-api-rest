from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.person_list, name='person_list'),
    path('<int:pk>/info', views.person_detail, name='person_detail'),
]