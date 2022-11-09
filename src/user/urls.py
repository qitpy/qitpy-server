"""
URL mapping for user API
"""
from django.urls import path
from knox import views as knox_views
from user import views

app_name = 'user'
urlpatterns = [
    path(
        'register-by-access-token/social/google-oauth2/',
        views.LoginWithGoogle.as_view(),
        name='login_with_google'
    ),
    path('authentication-test/', views.authentication_test),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path(
        'logoutall/',
        knox_views.LogoutAllView.as_view(),
        name='knox_logoutall'
    ),
]
