from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import os,sys
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render


from .models import *
from .Util import *
from datetime import *

from django.urls import reverse

from datetime import datetime
from django.core import serializers


@login_required(login_url='/login/')
def Printing(request, jobid):
    if(request.user.is_superuser):
        #Job.objects.filter(job_id=jobid).update(status='Printing')
        return HttpResponse("Ok")

    
@login_required(login_url='/login/')
def getPrintingList(request):   
    printing=[]
    if request.user.is_superuser:        
        printing = list(Job.objects.filter(status = "Printing").select_related("fk_profile"))     
    
    return HttpResponse(
        serializers.serialize("json", printing, fields=('job_id','job_title','file_path_stl','print_end_time' )),
        content_type="application/json"
    )

   
    
    





