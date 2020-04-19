from django.shortcuts import render
from walkapp.forms import Inputform,Registerform
from . import models
from django.contrib.auth.models import User
from walkapp.models import Mytimein,Wts_table
import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from tablib import Dataset
from walkapp.resources import Wtsresource

from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,UpdateView)


from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
import csv

# General way of displaying template*************************************************
def index(request):
    current = request.user
    notify = Wts_table.objects.filter(allocatedto=current)
    notify_dict = {'tableinfo': notify}
    return render(request,'index.html', context=notify_dict)
# General way of displaying template**************************************************

# Load the template file************Templateview method*******************************
@method_decorator(login_required, name='dispatch')
class Tool(TemplateView):
    template_name = 'toolupdate.html'
# Load the excel file******************************************************************

# Registration information*************************************************************
@method_decorator(login_required, name='dispatch')
class Registrationinfo(TemplateView):
    template_name = 'registrationinfo.html'
# Registration information*************************************************************

# Listing all the ASINs***************************************************************
@method_decorator(login_required, name='dispatch')
class Wts_tableListView(ListView):
    context_object_name = 'wts_list'
    model = models.Wts_table
    def get_queryset(self):
        current = self.request.user
        # todaydate = datetime.date()
        return Wts_table.objects.filter(allocatedto = current).filter(asintitleguideline__isnull = True).order_by('-allocationdate')
# Listing all the ASINs***************************************************************

# Update View*************************************************************************
@method_decorator(login_required, name='dispatch')
class Wts_tableupdateView(UpdateView):
    model = models.Wts_table
    # context_object_name = 'update'
    fields = ['Asinsitestatus',	'asinsearchable',	'comment1' ,	'asinretailcontribution',	'comment2',	'asinobsolete',	'comment3',	'asincurrentcategory',	'asincorrectcategory',	'comment4',	'item_name',	'asinreflectproduct',	'comment5',	'asinnomismatchbtwnattributes',	'comment6',	'asintitleguideline',	'comment7',	'asinmainimage',	'comment8'
              ,'comment9','asinimageborderwatermanrtextcheck',	'comment10',	'asinimagematchtitle',	'comment11',	'asinimagematchcolorsize',	'comment12',	'asinimageplaceholdercheck',	'comment13',	'asinimagegraphratings',	'comment14',	'asinimagepromotextcheck',	'comment15',	'asinimagecustomerdepict',	'comment16',
              'brand_name',	'asinbrandnamecorrect',	'comment17',	'asinbrandhyperlink',	'comment18',	'bullet_point1',	'bullet_point2',	'bullet_point3',	'bullet_point4',	'bullet_point5',	'bullet_point6',	'bullet_point7',	'bullet_point8',	'asinbulltpointrelevant',	'comment19',	'asinbulletwarrantyinfo',
              'comment20',	'asinbulletshort',	'comment21',	'asinbulletnumerals',	'comment22',	'asinsitemsg',	'asinreleasedate1',	'comment23',	'asinvariationcheck',	'comment24',	'color_name',	'asincolorname',	'comment25',	'size_name',	'asinsizecheck',	'comment27',	'asinnotorphan',	'comment28',	'asinsiteadescstatus',	'comment29',
              'asinapluscontent',	'comment30','asinrelevantproduct',	'comment31',	'asinappropriate',	'comment32',	'asin_subject_keywords',	'asinkeyword',	'comment33',	'asinvariationword',	'comment34',	'asinleafnode',	'comment35','asinmainimagewhitebg','asin','vendorCode','allocatedto','allocationdate' ]
              # ,'asin','vendorCode','allocatedto','allocationdate'
# Update View*************************************************************************

# Current Detail View*****************************************************************
class Wts_tableDetailView(DetailView):
    template_name = 'walkapp/detailview.html'
    context_object_name = 'wts_detail'
    model = models.Wts_table
# Current Detail View*****************************************************************

# Detail View*************************************************************************
# class Wts_tableDetailView(DetailView):
#     template_name = 'walkapp/detailview.html'
#     context_object_name = 'wts_detail'
#     model = models.Wts_table
# Detail View*************************************************************************

# Export data to csv
def export(request):
    wts_resource = Wtsresource()
    current = request.user
    data = Wts_table.objects.filter(allocatedto=current)
    dataset = wts_resource.export(data)
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="WTS_data_recommendations.csv"'
    return response
    # def get_queryset(self):
    #     current = request.user
    #     return Wts_table.objects.filter(allocatedto = current)

#Registrations code @kragha***********************************************************
def registration(request):
    registered = False
    if request.method == 'POST':
        regit = Registerform(data=request.POST)
        otherip = Inputform(data=request.POST)
        if regit.is_valid() and otherip.is_valid() :
            reginf = regit.save(commit=False)
            reginf.set_password(reginf.password)
            reginf.is_active = False
            reginf.save()
            otherinf = otherip.save(commit=False)
            otherinf.user = reginf
            otherinf.save()
            registered = True
            print("Registraion made at {}".format(timezone.now()))
        else:
            print(regit.errors,otherip.errors)
    else:
        regit = Registerform()
        otherip = Inputform()
    return render(request, 'register.html', context={'registered': registered,
                                                     'registerinfo': regit,
                                                     'otherip':otherip})
#Registrations code @kragha***********************************************************

# Login user @kragha******************************************************************
def loguser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_authenticated:
            if user.is_active:
                login(request, user)
                # Save a record when a person is logging in @kragha
                Timinginfo = Mytimein()
                Timinginfo.user = request.user
                Timinginfo.date = timezone.now()
                Timinginfo.save()
                # Save a record when a person is logging in @kragha
                # Display in terminal who has loggedin @kragha
                print("The user {} has logged-in at {}".format(username, timezone.now()))
                # Display in terminal who has loggedin @kragha
                return HttpResponseRedirect(reverse(index))
            else:
                return HttpResponse("<h1> <em> <b> Your account is not activated, contact @kragha </b> </em> </h1>")
        else:
            print("Invalid username: {} and password: {} used".format(username,password))
            return HttpResponse("<h1> <em> <b> Mr {} You have either entered incorrect username or password, please recheck </b> </em> </h1>".format(username))
    else:
        return render(request, 'login.html')
# Login user @kragha******************************************************************

# Change Password @kragha*************************************************************
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect(index)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {
        'form': form
    })
# Change Password @kragha*************************************************************

# Logout user @kragha******************************************************************
@login_required
def logguserout(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))
# Logout user @kragha******************************************************************

# Load the excel file******************************************************************
@login_required
def simple_upload(request):
    if request.method == 'POST':
        # class name of the resource function
        wts_data = Wtsresource()
        dataset = Dataset()
        new_upload = request.FILES['myfile']
        imported_data = dataset.load(new_upload.read())
        result = wts_data.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            wts_data.import_data(dataset, dry_run=False)  # Actually import now
            print("Data uploaded successfully at {}".format(timezone.now()))
        else:
            return HttpResponseRedirect(reverse("Error"))
    else:
        wts_data = Wtsresource()
        dataset = Dataset()
    return render(request, 'load.html')
# Load the excel file******************************************************************

# Error when file is loaded************************************************************
class Error(TemplateView):
    template_name = 'error.html'
# Error when file is loaded************************************************************
