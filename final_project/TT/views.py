from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from django.http import HttpResponse, Http404
from mimetypes import guess_type
import time
from TT.models import *
from TT.forms import *

# Create your views here.
def home(request):
	context = {}
	return render(request, 'base.html', context)



def register(request):
    context = {}
    # Just display the registration form if this is a GET request
    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'TT/register.html', context)

    form = RegistrationForm(request.POST)
    print "form created"
    context['form'] = form
    if not form.is_valid():
    	print "form not valid"
        return render(request, 'TT/register.html', context)
    print "form valid"
    # Creates the new user from the valid form data
    new_user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password1'],
                                        email=request.POST['email'],
                                        first_name=request.POST['firstname'],
                                        last_name=request.POST['lastname'])
    new_user.is_active=False
    print "new user created"
    new_user.save()
    print "new user saved"
    token=default_token_generator.make_token(new_user)

    new_token = UserToken(token=token,user=new_user)
    new_token.save()

    mailbody="""Welcome to TT. Please click the following to confirm your email address:

                http://%s/TT/confirm?t=%s&u=%s
                """ % (request.get_host(),token,new_user.username)

    send_mail(subject="Verify your email address from TinyBlog",
              message=mailbody,
              from_email="lli@andrew.cmu.edu",
              recipient_list=[new_user.email])
    # Logs in the new user and redirects to his/her todo list
    new_user = authenticate(username=request.POST['username'],
                            password=request.POST['password1'])
    print "new user authenticated"
    login(request, new_user)
    print "new user logined"
    context['email']=new_user.email
    return render(request,'TT/need-confirmation.html',context)

def confirmEmail(request):
    context={'verify':False}
    if 'u' in request.GET and 't' in request.GET:
        username=request.GET['u']
        token=request.GET['t']

        user=User.objects.filter(username__exact=username)
        if user:
            if UserToken.objects.filter(user=user,token=token):
                user[0].is_active=True
                user[0].save()
                context['verify']=True
                return render(request,"TT/confirm.html",context)
    
    return render(request,"TT/confirm.html",context)




