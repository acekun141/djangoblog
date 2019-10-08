from django.shortcuts import render
from .models import Post
from django.views import View

# Create your views here.

class HomeView(View):
	template = 'home/index.html'
	def get(self, request):
		posts = Post.objects.all().order_by('-time')
		return render(request, self.template, {'posts':posts,'title':'Home'})