from django.shortcuts import render,redirect
from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Count
from django.contrib import messages


def Admin_Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/admin_view')
        else:
            messages.success(request, 'invalid Password or Username')
            return redirect( "/admin_login")

    return render(request, 'admin_login.html')

def Admin_view(request):
    if request.user.is_superuser:
        return render(request, 'admin_view.html')
    else:
        messages.success(request, 'Admin profile does not exist !')
        return redirect('/admin_login/')
    
def Available_Donors(request):
    all_group = BloodGroup.objects.annotate(total=Count('donor'))
    return render(request,'available_donors.html',{'all_group': all_group})
 
def Patient_blood_request(request):
    requests = RequestBlood.objects.all()
    return render(request,'patient_blood_request.html',{'requests':requests})


def Patient_blood_approve(request,request_id):
    request=RequestBlood.objects.get(id=request_id)
    request.status=1
    request.save()
    return redirect('/patient_blood_request/')
    

def Patient_blood_disapprove(request,request_id):
    request=RequestBlood.objects.get(id=request_id)
    request.status=2
    request.save()
    return redirect('/patient_blood_request/')

def Donor_blood_approve(request,request_id):
    request=Donate_Blood.objects.get(id=request_id)
    request.status=1
    request.save()
    return redirect('/donate_history/')
    

def Donor_blood_disapprove(request,request_id):
    request=Donate_Blood.objects.get(id=request_id)
    request.status=2
    request.save()
    return redirect('/donate_history/')

def donor_list(request): 
    donors = Donor.objects.all()                  
    return render(request,'donor_list.html',{'donors':donors})
 
def delete_donor(request,id): 
    donor = Donor.objects.get(pk=id)
    user = donor.donor       
    donor.delete()
    user.delete()
    messages.success(request,"Donor Deleted Successfully")
    return redirect('donor_list')
 
def patient_list(request): 
    patients = Patient.objects.all()                  
    return render(request,'patient_list.html',{'patients':patients})
 
def delete_patient(request,id): 
    patient = Patient.objects.get(pk=id)
    user = patient.patient       
    patient.delete()
    user.delete()
    messages.success(request,"Patient Deleted Successfully")
    return redirect('patient_list')

def patient_details(request,id):
    patient_profile = Patient.objects.get(pk=id)
    user=patient_profile.patient
    return render(request, "patient_details.html", {'patient_profile':patient_profile,'user':user})