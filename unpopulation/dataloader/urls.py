from django.urls import path, include
from . import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls',
         namespace='rest_framework')),
    path('', views.home, name="home_page"),
    path('first/', views.first, name="first_api"),
    path('home/', views.first_view, name="first_view"),

    path('home2/', views.second_view, name="second_view"),
    path('second/', views.second, name="second_api"),

    path('home3/', views.third_view, name="third_view"),
    path('third/', views.third, name="third_api"),

    path('home4/', views.fourth_view, name="fourth_view"),
    path('fourth/', views.fourth, name="fourth_api"),
]
