from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from testapp.forms import LoginForm

def saikrishna(request):
	return render(request,'testapp/index.html')

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    #print("User logged in :",request.user.is_authenticated())
    #print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username  = form.cleaned_data.get("username")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        #print(request.user.is_authenticated())
        if user is not None:
            #print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            #context['form'] = LoginForm()
            return redirect("/saikrishnateja")
        else:
            # Return an 'invalid login' error message.
            print("invalid username or password")

    return render(request, "auth/login.html", context)	

# Create your views here.
