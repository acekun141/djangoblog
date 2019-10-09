from django.shortcuts import render
from .models import Post
from django.views import View
from .forms import PostForm
import uuid

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
		try:
			post = Post.objects.get(uuid=uuid)
		except:
			pass
		
		return render(request, self.template, {'post':post})

class CreatePost(View):
	template = 'home/createpost.html'
	form = PostForm()
	def get(self, request):

		return render(request, self.template, {'form':self.form})

	def post(self, request):
		postform = PostForm(request.POST, request.FILES)
		if postform.is_valid():
			postform.save()

		return render(request, self.template, {'form':self.form})

class EditPost(View):
	template = 'home/editpost.html'

	def get(self, request, uuid):

		try:
			post = Post.objects.get(uuid=uuid)

			return render(request, self.template, {'post':post})
		except:
			pass
		


