from django.urls import path

from crud_web import views

urlpatterns = [
    path('welcome', views.welcome_django),
    path('home', views.home_page),
    path('about-us', views.about_us),
    path('person', views.persons),
    path('person/<str:uuid>', views.person),
    path('address', views.address)
]
