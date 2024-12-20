from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .views.users_view import user_list, user_detail

from api.users_api.views import (
    LoginView,
    LogOutView,
    RegistrationView,
    MeView
)

urlpatterns = [
    path('login/', csrf_exempt(LoginView.as_view())),
    path('logout/', csrf_exempt(LogOutView.as_view())),
    path('registration/', csrf_exempt(RegistrationView.as_view())),
    path('me/', login_required(MeView.as_view())),
    path('', user_list),
    path('<int:pk>', user_detail),
]