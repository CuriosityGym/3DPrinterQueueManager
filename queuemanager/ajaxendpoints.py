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
    

      
    printingList=[]
    
    if request.user.is_superuser:
        
        printing = list(Job.objects.filter(status = "Printing").select_related("fk_profile"))       
        for i in range(0, len(printing)):
            printingList.append(printing[i])

        

    else:
        
        printing = list(Job.objects.filter(status = "Printing").filter(fk_profile = util.getProfile(request.user)))
 
        for i in range(0, len(printing)):
            printingList.append(printing[i])

    

    for i in range(0, len(printingList)):
        printingList[i].endDate = printingList[i].print_end_time.strftime("%d %b %Y")
    

    util = Util()
    context = util.getQuota(request.user)   
    context['PrintingContextObject'] = printingList
    return HttpResponse(
        serializers.serialize("json", context),
        content_type="application/json"
    )

   
    
    





