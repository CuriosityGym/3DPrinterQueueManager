from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import os,sys
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import *
from .Util import *
from datetime import *

from django.urls import reverse

from datetime import datetime
from django.core import serializers
from django.template.loader import render_to_string


@login_required(login_url='/login/')
def Printing(request, jobid):
    if(request.user.is_superuser):        
        Job.objects.filter(job_id=jobid).update(status='Printing')
        return HttpResponse("Ok")

    
@require_http_methods(["GET", "POST"])
@login_required(login_url='/login/')
def PrintedCompleted(request, jobid):
    if(request.user.is_superuser):
        printTime = request.POST['printTime']
        Job.objects.filter(job_id=jobid).update(status='Printed',print_time=printTime)
        return HttpResponse("Ok")

    
@require_http_methods(["GET", "POST"])
@login_required(login_url='/login/')
def PrintedFailed(request, jobid):
    if(request.user.is_superuser):
        Job.objects.filter(job_id=jobid).update(status='Failed',print_time=60)
        return HttpResponse("Ok")

    
@login_required(login_url='/login/')
def getPrintingList(request):
    util = Util()
    context = util.getQuota(request.user)
    printingList=[]
    if request.user.is_superuser:        
        printing = list(Job.objects.filter(status = "Printing").select_related("fk_profile"))        
        for i in range(0, len(printing)):
            printingList.append(printing[i])
        for i in range(0, len(printingList)):
            printingList[i].endDate = printingList[i].print_end_time.strftime("%d %b %Y")       
    context['PrintingContextObject'] = printingList
    return render(request, 'printingDataTemplate.html', context)


@login_required(login_url='/login/')
def getStatistics(request):
    util = Util() # Get access to UTIL
    context = util.getQuota(request.user) #Get quota
    jobData=list(Job.objects.all()) #Get data of all jobs, change this for your custom statistics
    context["jobdata"]=jobData # assign it to some context list
    
    myJsonText=render_to_string('my_json_template.html', context) #this template basically allows you to generate your json structure as text
    return HttpResponse(myJsonText, content_type='application/json') #return the json text as formatted json 
        

   
    
    





