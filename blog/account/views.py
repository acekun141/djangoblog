from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
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
            if (username and password):
              user = authenticate(username=username,
                                  password=password)
              if not user:

                raise "Tài khoản không tồn tại!"

              else:
                login(request, user)

                return HttpResponseRedirect("/")

        except:
            return render(request,
                          self.template,
                          {'title':self.title,
                               'error':True})
        return render(request, self.template,  {'title':self.title})


# class SignupView(View):
#     template = 'account/signup.html'
#     title = 'Login'
#     def get(self, request):
        
#         return render(request, self.template,  {'title':self.title})

#     def post(self, request):
#         try:
#             username = request.POST['username']
#             email = request.POST['email']
#             password1 = request.POST['password1']
#             password2 = request.POST['password2']
#             if (username and email 
#                and password1 and password2):          
#               if (password1 == password2):
#                 try:
#                   User.objects.get(username=username)

#                   raise Exception("Tài khoản đã tồn tại!")
#                 except ObjectDoesNotExist:
#                   pass
#               else:

#                 raise Exception("Mật khẩu không khớp!")
#             else:

#               raise Exception("Vui lòng điền đủ các trường!")

#             User.objects.create_user(username=username,
#                                      password=password1,
#                                      email=email)

#             return HttpResponseRedirect('/')
#         except Exception as value:
#             return render(request,
#                           self.template,
#                           {'title':self.title,
#                                'error':value})

class LogoutView(View):
    def get(self, request):
      logout(request)

      return HttpResponseRedirect('/')
    
    