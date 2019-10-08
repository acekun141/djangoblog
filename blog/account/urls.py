from django.urls import path
from .views import LoginView, SignupView

urlpatterns = [
    path('login/', LoginView.as_view(), name='signin'),
    path('signup/', SignupView.as_view(), name='signup'),
]
