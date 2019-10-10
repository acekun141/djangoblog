from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import Post, Image
from django.views import View
from .forms import PostForm, SaveImage
import uuid
import os
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
		form = SaveImage()
		if not request.user:

			return HttpResponseRedirect('/')
		try:
			post = Post.objects.get(uuid=uuid)
			print(post.image.path)

			return render(request, self.template, {'post':post, 'form':form})
		except:
			pass
	
	def post(self, request, uuid):
		try:
			new_title = request.POST.get("title")
			new_content = request.POST.get("content")
			image = SaveImage(request.POST ,request.FILES)
			if image.is_valid():
				new_image = image.save()
				post = post.objects.get(uuid=uuid)
				if os.path.isfile(post.image.path):
					os.remove(path)
				Post.objects.filter(uuid=uuid).update(title=new_title,
													  content=new_content,
													  image=new_image.image)
			else:
				print({'error:':image.errors})
			return redirect('singlepost', uuid=uuid)
		except Exception as value:
			print(value)

			return HttpResponseRedirect('/')
		


