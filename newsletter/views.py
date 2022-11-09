from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Newsletter
import re

def validate_email_address(email_address):  
   return re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email_address)

# Create your views here.
def news (request):
  if request.method == 'POST':
    obj = Newsletter()
    obj.email = request.POST['email']
    if validate_email_address(obj.email):
      if Newsletter.objects.get(email=obj.email):
        messages.success(request, 'You already have a subscription!')
      else:
        obj.save()
        messages.success(request, 'Successfully subscribed to newsletter!')
      return redirect('home')
    else:
      messages.error(request, 'Enter a valid email address!!')
      return redirect('home')
  else:
    return redirect('home')