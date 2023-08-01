from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import LoginForm
from . import views
app_name="Eapp"
urlpatterns=[
    path('home/',views.index,name="home"),
    path('contact/',views.contact,name="contact"),
    path('signup/',views.signup,name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='Eapp/login.html', authentication_form=LoginForm), name='login'),
]