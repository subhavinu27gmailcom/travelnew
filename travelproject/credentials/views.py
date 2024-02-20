from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
def logout(request):
        auth.logout(request)
        return redirect('/')
def register(request):
        if request.method=="POST":
                username =request.POST["username"]
                lname=request.POST["lname"]
                fname=request.POST["fname"]

                pass1 = request.POST['pass1']

                pass2 = request.POST['pass2']
                email = request.POST['email']
                if pass1==pass2:
                        if User.objects.filter(username = username).exists():
                                messages.info(request, "username taken")
                                print("username taken")
                                return redirect("/credentials/register")
                        elif User.objects.filter(email =email).exists():
                                messages.info(request,"email taken")
                                print("email taken")
                                return redirect("/credentials/register")
                        else:

                                user = User.objects.create_user(username=username,email=email,password=pass1,last_name=lname,first_name=fname)
                                user.save()
                                print("usercreated")

                                return redirect("/credentials/login")
                else:
                        print("password not matching")
                        messages.info(request, "password not matching")
                        return redirect("/credentials/register")

        return render(request, "register.html")
def login(request):
        if request.method == "POST":
                username = request.POST["username"]
                pass1 = request.POST["pass1"]
                user=auth.authenticate(request,username=username,password=pass1)
                if user is not None:
                        auth.login(request,user)
                        return redirect("/")
                else:
                        messages.info(request, "invalid username or password")
                        print("invalid username or password")
                        return redirect("/credentials/login/")
        return render(request, "login.html")
