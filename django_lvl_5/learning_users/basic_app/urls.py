from django.urls import include, path
from basic_app import views

# template urls!

app_name = 'basic_app'

urlpatterns=[
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
