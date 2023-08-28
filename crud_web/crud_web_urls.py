from django.urls import path

from crud_web import views

urlpatterns = [
    path('', views.home_page),
    path('about', views.about_us),
    path('person', views.all_persons),
    path('person/<str:uuid>', views.get_person),
    path('address', views.address),
    path('create', views.default_data)
]
