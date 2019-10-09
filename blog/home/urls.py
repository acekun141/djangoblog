from django.urls import path
from .views import HomeView, PostView, CreatePost

urlpatterns = [
	path('', HomeView.as_view(), name='homepage'),
	path('post/<str:uuid>', PostView.as_view(), name='singlepost'),
	path('createpost', CreatePost.as_view(), name='createpost'),
	# path('post/edit', PostView.as_view(), name='singlepost'),
]