import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.models import User, auth
from django.http import HttpResponse



# Create your views here.
def login(request):
    return render(request,"login.html")


def signup(request):
    return render(request,"signup.html")


class create_user(APIView):
    def post(self, request):
        data=request.data
        print(data)

        obj=User.objects.filter(username = data.get('user_name'))
        if obj:
            result = json.dumps({"message": "Username already exist"})
            return HttpResponse(result, status=500)
        user = User.objects.create_user(first_name = data.get('first_name'),
                                        last_name = data.get('last_name'),
                                        username = data.get('user_name'),
                                        email = data.get('user_name'),
                                        password = data.get('password'))
        user.save()
        return HttpResponse("Success", status=200)


class login_user(APIView):
    def post(self,request):
        data=request.data
        print(data)
        user = auth.authenticate(username = data.get('username'), password = data.get('password'))
        if user :
            auth.login(request, user)
            return HttpResponse('Success', status=200)
        return HttpResponse(status=500)


def logout_user(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect("/")




