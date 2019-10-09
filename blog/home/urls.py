from django.urls import path
from .views import HomeView, PostView, CreatePost, EditPost

urlpatterns = [
	path('', HomeView.as_view(), name='homepage'),
	path('post/<str:uuid>', PostView.as_view(), name='singlepost'),
	path('createpost', CreatePost.as_view(), name='createpost'),
	path('editpost/<str:uuid>', EditPost.as_view(), name='editpost'),
]