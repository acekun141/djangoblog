from django.urls import path
from .views import HomeView, PostView

urlpatterns = [
	path('', HomeView.as_view(), name='homepage'),
	path('<str:uuid>', PostView.as_view(), name='singlepost'),
]