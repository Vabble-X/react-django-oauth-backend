from django.conf.urls import url
from django.urls import path
from users import views
 
app_name = 'auth'

urlpatterns = [
    path('api/auth', views.user_authontication),
    url(r'^api/auth/(?P<pk>[0-9]+)$', views.user_authontication, name='user_authontication'),
    path('api/user_data', views.get_user_data),
    url(r'^api/user_data/(?P<pk>[0-9]+)$', views.get_user_data, name='get_user_data'),
]
