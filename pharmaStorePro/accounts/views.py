
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from django.template import loader

from . models import *
 
# Create your views here.
def register(request):
    if request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        cpwd = request.POST['password2']
        if password == cpwd:
            if User.objects.filter(username=username).exists():
                messages.info(request, "⚠️ Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "⚠️ Email already taken")
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)  #add ob...create_user thats why password encrpated
                user.save()

        else:
            messages.info(request, "⚠️ Password Not Match")
            return redirect('register')
        return redirect('login')
    else:
        return render(request, 'register.html')



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.username != "admin":
                auth.login(request, user)  # Use auth_login to log in the user(auth.login)
                request.session['uid'] = user.id
                request.session['username'] = user.username
                return redirect('/')
            else:
                return redirect('/admin_home')
        print(user)    
    return render(request, 'login.html')


# def staff_login(request):
#     if request.method == 'POST':
#         form = staffLoginForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None and hasattr(user, 'staffuser'):
#                 auth.login(request, user)
#                 request.session['staff_user_id'] = user.staffuser.id
#                 return redirect('/staff/staffhome')
#     else:
#         form = staffLoginForm()

#     return render(request, 'staffLogin.html', {'form': form})


def staff_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        staff_member = StaffUser.objects.filter(username=username, password=password).first()
        if staff_member is not None:
            # Successful login, redirect to the staff dashboard
            return redirect('/staff/staffhome')  # Redirect to the staff dashboard or wherever you want
        else:
            # Handle invalid login credentials, e.g., display an error message
            return render(request, 'staffLogin.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'staffLogin.html')

# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         if User.objects.filter(username=username, password=password):
#             data = User.objects.get(username=username, password=password)
#             if data.username != "admin":

#                 request.session['uid'] = data.id
#                 request.session['username'] = data.username
#                 template = loader.get_template('index.html')
#                 context = {'session': request.session['username']}
#                 return HttpResponse(template.render(context, request))
#             # elif data.username=="admin":
#             #     template = loader.get_template('admin_home.html')
#             #     context = {}
#             #     return HttpResponse(template.render(context,request))
#             else:
#                 return redirect('/user_home')
#     return render(request, 'login.html')

# # ----------
# def staff_login(request):
#     if request.method == 'POST':
#         form = staffLoginForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None and hasattr(user, 'staffuser'):
#                 auth.login(request, user)
#                 request.session['staff_user_id'] = user.staffuser.id
#                 print(request.session['staff_user_id'])  # Add this line for debugging
#                 return redirect('staff_dashboard')
#     else:
#         form = staffLoginForm()

#     return render(request, 'staffLogin.html', {'form': form})
# -----------




def staff_dashboard(request):
    context = {'username': request.user.username}
    return render(request, 'staffhome.html', context)

# def user_home(request):
#     context = {'username': request.user.username}
#     return render(request, 'index.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')