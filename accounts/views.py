from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout, login

def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()#we save as well as get data
            login(request,user)
            return redirect('fronted:home')
        else:
            form=UserCreationForm()
            return render(request,'signup.html',{'form':form})
    else:
        form =UserCreationForm(request.POST)
    
    return render(request,'signup.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        signin_form=AuthenticationForm(data=request.POST)
        if signin_form.is_valid():
            user=signin_form.get_user()
            login(request,user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('fronted:home')
    else:
        signin_form=AuthenticationForm()
    return render(request,'login.html',{'signin_form':signin_form})#we are sending this as response to request

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('fronted:home')
    else:
        logout(request)
    return redirect('fronted:home')