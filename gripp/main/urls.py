from django.urls import path
from . import views
urlpatterns = [
    path('', views.main),
    path('articles/', views.articles),
    path('profile/', views.profile),
    path('map/', views.map),
]
