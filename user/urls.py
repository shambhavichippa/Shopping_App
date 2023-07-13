from django.urls import path
from user import views

urlpatterns=[
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('create_user', views.create_user.as_view()),
    path('user_authenticate', views.login_user.as_view()),
    path('logout', views.logout_user)
]