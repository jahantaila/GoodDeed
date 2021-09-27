from django.contrib.auth.models import User
from django.http import request
from django.http.request import RAISE_ERROR
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import forms, inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.db.models import F
from home import models
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from home.models  import Contact, Donation, Request, UserDetail
import datetime
from django.views.generic import DetailView
from django.core.mail import message, send_mail
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
import time 
from django.db.models import Sum

from django.forms import ModelForm
# Create your views here.

def index(request,*args, **kwargs):
  return render(request, "index.html", {} )



@login_required(login_url='/login/')
def dashboard(request):
    user = request.user
    # assuming there is exactly one
    # this will break if there are multiple or if there are zero
    # You can (And should) add your own checks on how many userdetails objects you have for the user
    # consider using a OneToOneField instead of a ForeignKey
    user_details = UserDetail.objects.get(user=user)  # or userdetails.objects.get(user=user)
    context = {
        "donations": user_details.donations,
        "points": user_details.points,
        "requests": user_details.requests,
    }
    return render(request,'dashboard.html', context=context)


  

def register(request, ):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    else: 
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                UserDetail.objects.create(
                    donations=0,
                    points=0,
                    requests = 0,
                    user=user
                )
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your account has been successfully created, {username} ')
                return redirect('loginpage')
        context = {'form': form}
        return render(request, "register.html",  context )



def loginpage(request):
	if request.user.is_authenticated:
		return redirect('/dashboard/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/dashboard')
			else:
        
				messages.error(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutuser(request):
	logout(request)
	return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def donate(request):
    if request.method == "POST":
        title = request.POST['donationtitle']
        phonenumber = request.POST['phonenumber']
        category = request.POST['category']
        quantity = request.POST['quantity']
        location = request.POST['location']
        description = request.POST['description']
        date = datetime.datetime.now().date()
        ins = Donation(title = title, phonenumber = phonenumber, category = category, quantity = quantity, location = location, description = description, user=request.user, date = date,   )
        ins.image=request.FILES['image']
        ins.save()
        # New part. Update donor's stats.
        UserDetail.objects.filter(user=request.user).update(donations=F('donations') + 1)
        UserDetail.objects.filter(user=request.user).update(points=F('points') + (quantity * 2))
        return HttpResponseRedirect( '/thankyou/', )
    return render(request,'donate.html')

@login_required(login_url='/login/')
def availablesupplies(request):
    donations = Donation.objects.all()
    context = {'donations':donations}
    return render(request, 'availablesupplies.html', context)


@login_required(login_url='/login/')
def thankyou(request):
    return render(request,'thankyou.html')





def deleteDonation(request, id=None):
    donation = get_object_or_404(Donation, pk=id)
    time.sleep(6)
    donation.delete()
    return redirect('/dashboard/')



    
    

#thing to show donations on acceptdonate.html
class DonationDetail(DetailView):
    model = Donation
    queryset = Donation.objects.all()
    template_name = 'acceptdonation.html' # whatever template name you want



def about(request):
    return render(request, 'about.html')

@login_required(login_url='/login/')
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        content = request.POST['content']
        date = datetime.datetime.now().date()
        ins = Contact( name = name, subject = subject, email = email, content = content, date = date,    )
        ins.save()
        time.sleep(2)
        return redirect( '/dashboard/')        
    return render(request, 'contact.html')

@login_required(login_url='/login/')
def request(request):
    if request.method == "POST":
        title = request.POST['requestitle']
        phonenumber = request.POST['phonenumber']
        category = request.POST['category']
        quantity = request.POST['quantity']
        location = request.POST['location']
        description = request.POST['description']
        date = datetime.datetime.now().date()
        ins = Request(title = title, phonenumber = phonenumber, category = category, quantity = quantity, location = location, description = description, user=request.user, date = date,   )
        ins.image=request.FILES['image']
        ins.save()
        messages.success(request, f'Your {title} has been requested successfully.  ')
        return HttpResponseRedirect( '/dashboard/', )
    return render(request, 'request.html')


def viewrequests(request):
    requests = Request.objects.all()
    context = {'requests':requests}
    return render(request, 'viewrequests.html', context)

class RequestDetail(DetailView):
    model = Request
    queryset = Request.objects.all()
    template_name = 'acceptrequest.html'

def deleteRequest(request, id=None):
    userrequest = get_object_or_404(Request, pk=id)
    time.sleep(6)
    UserDetail.objects.filter(user=request.user).update(points=F('points') + (userrequest.quantity * 2) + 100)
    userrequest.delete()
    return redirect('/dashboard/')

def leaderboard(request,):
    leaders = User.objects.annotate(
        total_points=Sum('userdetail__points')
    ).order_by('-total_points')[:10000000]

    return render(request, 'leaderboard.html', {'leaders': leaders})

