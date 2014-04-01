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



