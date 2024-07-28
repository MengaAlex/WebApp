from django.urls import path, re_path
from . import views
 
# Регистрация функций отображения
urlpatterns = [
    path('', views.index, name='home'),
    path('entrance', views.entrance, name='entrance'),
    path('profile', views.profile, name='profile'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop')
]
 
