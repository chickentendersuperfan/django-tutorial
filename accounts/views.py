from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):

    if request.method == 'POST':   
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # TODO: show alert to web page
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                # Create user object
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'User created')
                return redirect('login')
        else:
            messages.info(request, 'Passwords not matched')
            return redirect('register')

        return redirect('/travello')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':   
        username = request.POST['username']
        password = request.POST['password']

        # Get the user object
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('logged in!')
            return redirect('/travello')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
        
    else:
        return render(request, 'login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('/travello')