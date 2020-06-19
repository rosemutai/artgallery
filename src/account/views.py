from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
  context = {}
  return render(request,'account/login.html',context)



def registration_view(request):
  context ={}
  return render(request,'account/register.html')


def logout_view(request):
  context ={}
  return redirect('/')