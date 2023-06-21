from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Login
from .models import Formregister


# Create your views here.

# HOME_PAGE
def index(request):
    return render(request,'index.html')

#registering
def register(request):
    if request.method== 'POST':    #fetching data from form
        username=request.POST['username']
        # email = request.POST['email']
        password = request.POST['password1']
        cpassword = request.POST['password2']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('schoolapp:register')
            else:
                user = User.objects.create_user(username=username, password=password)
            user.save();
            return redirect('schoolapp:login')
            # print("User created")

        else:
            messages.info(request, "Password not matching")
            return redirect('schoolapp:register')
        return redirect('/')
    return render(request, "register.html")


#login page
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/form')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('schoolapp:login')
    return render(request, "login.html")

#registring page of store items
def form(request):
    if request.method=='POST':
        fname=request.POST.get('fn','')
        lname = request.POST.get('ln', '')
        address = request.POST.get('address', '')
        dob = request.POST.get('dob', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        phoneno = request.POST.get('phno', '')
        email = request.POST.get('email', '')
        dept = request.POST.get('dept', '')
        course = request.POST.get('status', '')
        purpose = request.POST.get('purpose', '')
        # materials = request.POST.getlist('checkbox_data')
        form=Formregister(fname=fname,lname=lname,address=address,dob=dob,age=age,gender=gender,phoneno=phoneno,email=email,dept=dept,course=course,purpose=purpose)
        form.save()
        messages.success(request, "Profile details successfully created")

        return redirect('/')
    return render(request,'form.html')

# Logout_from_page
def logout(request):
    auth.logout(request)
    return redirect('/')