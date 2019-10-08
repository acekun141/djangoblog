from django.shortcuts import render
from django.views import View
# Create your views here.

class LoginView(View):
    template = 'account/login.html'
    title = 'Login'
    def get(self, request):
        
        return render(request, self.template,  {'title':self.title})

    def post(self, request):
        try:
            username = request.POST['username']
            password = request.POST['password']
        
        except:
            return render(request,
                          self.template,
                          {'title':self.title,
                               'error':True})
        return render(request, self.template,  {'title':self.title})


class SignupView(View):
    template = 'account/signup.html'
    title = 'Login'
    def get(self, request):
        
        return render(request, self.template,  {'title':self.title})

    def post(self, request):
        try:
            username = request.POST['username']
            password1 = request.POST['password']
            password2 = request.POST['password']
        
        except:
            return render(request,
                          self.template,
                          {'title':self.title,
                               'error':True})
        return render(request, self.template,  {'title':self.title})