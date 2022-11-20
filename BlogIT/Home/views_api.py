from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import Profile
from .helpers import *
class LoginView(APIView):
    def post(self,request):
        response={}
        response['status']=500
        response['message']='Something went wrong!!'

        try:
            data = request.data
            _username = data.get('username')
            _password=data.get('password')
            if _username is None:
                response['message']='Username is not found!'
                raise Exception('Username not found!')
            if _password is None:
                response['message']='Password is not found!'
                raise Exception('Password is not found!')
            user_exists = User.objects.filter(username=_username)
            if len(user_exists)==0:
                response['message']='invalid user! - User not found'
                raise Exception('invalid user! - User not found')
            user_obj = authenticate(username=_username,password=_password)
            if user_obj:
                login(request, user_obj)
                response['status']=200
                response['message']='Login successful!'
            else:
                response['message']='invalid password!'
                raise Exception('invalid password!')

        except Exception as e:
            print(e,'----------')
            return Response(response)
        return Response(response)

class RegisterView(APIView):
    def post(self,request):
        response={}
        response['status']=500
        response['message']='Something went wrong!!'

        try:
            data = request.data
            _username = data.get('username')
            _password=data.get('password')
            if _username is None:
                response['message']='Username not found'
                raise Exception('Username not found!')
            if _password is None:
                response['message']='Password  not found!'
                raise Exception('Password  not found!')
            user_exists = User.objects.filter(username=_username)
            if len(user_exists)!=0:
                response['message']='User already exists! please login'
                raise Exception('User already exists! please login')
            user_obj = User.objects.create(email=_username,username=_username)
            user_obj.set_password(_password)
            user_obj.save()
            token=generate_random_string(10)
            Profile.objects.create(user=user_obj, token=token,
                                   is_verified=True)

            response['message']='User registered succesfully!'
            response['status']=200
            return Response(response)

        except Exception as e:
            print(e)
            return Response(response)
        # return Response(response)

