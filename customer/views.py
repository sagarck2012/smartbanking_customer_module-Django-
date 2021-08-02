from django.shortcuts import render
from django.shortcuts import render, redirect, Http404
from django.http import HttpResponse
from .models import *
from django.contrib import messages
import hashlib
from user_management.decorator import *
import sys
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.

@login_required
def customer_add(request):
    template = 'customer/customer_add.html'
    context = {

    }
    return render(request, template, context)
