from django.shortcuts import render
from .models import Post
from django.views import View

# Create your views here.

class HomeView(View):
	template = 'home/index.html'
	def get(self, request):
		posts = Post.objects.all().order_by('-time')

		return render(request, 
					  self.template,
					  {'title':'Home','posts':posts})

class PostView(View):
	template = 'home/post.html'
	def get(self, request, uuid):
		print(uuid)
		post = Post.objects.get(uuid=uuid)
		return render(request, self.template, {'post':post})