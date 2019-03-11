from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.method == "POST":
        if "SignIn" in request.POST:
            print(request.POST)
        if "SignUp" in request.POST:
            u = User(username=request.POST["username"], first_name=request.POST["name"], password=request.POST["password"], email=request.POST["email"])
            User.save(u)

    return render(request, template_name="index.html")
