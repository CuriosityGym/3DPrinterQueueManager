"""InnovationHubWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views,ajaxendpoints
from django.contrib.auth import views as auth_views

urlpatterns = [

    #admin
    path('admin/', admin.site.urls),

    #HomePage
    path('', views.HomePage),
    path('home/', views.HomePage),

    #Schedule
    path('schedule/', views.Schedule),
    path('printData/<int:jobid>', views.PrintData),
    path('printData/download/<int:jobid>', views.PrintDownload),

    #Submit
    path('submit/', views.Submission),
    path('submit/request/', views.Submission),
    path('submit/preview/', views.Preview),
    path('submit/request/success/', views.Success),
    path('submit/request/fail/', views.Fail),

    #Account
    path('account/', views.AccountData),
    path('account/data/', views.AccountData),
    path('account/edit/', views.EditAccount),
    #path('account/login/', auth_views.login, name='login'),
    #path('account/logout/', views.Logout),
    #path('accounts/login/', auth_views.LoginView.as_view()),


    #CarlSegment
    path('userGuides/', views.UserGuidePage),

    #Login
    path('login/', views.Login, name='login'),
    path('login/authenticate/', views.Authenticate),
    path('logout/', views.Logout, name='logout'),

    #FeaturedPrints
    path('featuredPrints/', views.Featured),

    #Layout
    path('layout/', views.Layout),

    #ADMIN
    path('ADMIN/', views.AdminHome),
    path('ADMIN/INCREASE_GRADE', views.IncreaseGrade),
    path('ADMIN/DECREASE_GRADE', views.DecreaseGrade),
    path('ADMIN/EXCEL', views.AdminExcel),
    path('infidel/', views.Infidel),

    path('studentFile/', views.ReturnStudentList),
    path('jobFile/', views.ReturnJobList),

    #Printer
    path('printer/<str:name>', views.Printer),
    path('printer/printed/<int:jobid>', views.Printed),
    path('printer/printing/<int:jobid>', views.Printing),

    #ajax requests end points
    path('changeJobStatus/printing/<int:jobid>', ajaxendpoints.Printing),
    path('getPrintingList/', ajaxendpoints.getPrintingList),
    path('changeJobStatus/completed/<int:jobid>', ajaxendpoints.PrintedCompleted),
    path('changeJobStatus/failed/<int:jobid>', ajaxendpoints.PrintedFailed),
    
    #testPaths
    path('viewSTL/<int:jobid>', views.viewSTL),
    path('stats/', ajaxendpoints.getStatistics),
    
]

#handler404 = 'views.error_404_view'
#handler500 = 'views.error_500_view'
