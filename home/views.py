from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from . models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .forms import EditProfileForm
from django.contrib import messages


def index(request):
    all_group = BloodGroup.objects.annotate(total=Count('donor'))
    return render(request, "index.html", {'all_group':all_group})

def donors_list(request, myid):
    blood_groups = BloodGroup.objects.filter(id=myid).first()
    donor = Donor.objects.filter(blood_group=blood_groups)
    return render(request, "donors_list.html", {'donor':donor})

def donors_details(request, myid):
    details = Donor.objects.filter(id=myid)[0]
    return render(request, "donors_details.html", {'details':details})

def request_blood(request):
    user = request.user
    patient=user.patient
    full_name = f"{user.first_name} {user.last_name}"
    
    if request.method == "POST":
        blood_group = request.POST['blood_group']
        date = request.POST['date']
        blood_requests = RequestBlood.objects.create(patient_id=request.user.id, name=full_name, email=user.email, phone=patient.phone, city=patient.dist, address=patient.address, blood_group=BloodGroup.objects.get(name=blood_group), date=date)
        blood_requests.save()
        messages.success(request, 'Blood Request Sent Successfully.')
        return redirect("request_blood")
    return render(request, "request_blood.html")

def see_all_request(request):
    requests = RequestBlood.objects.filter(patient_id=request.user.id)
    return render(request, "see_all_request.html", {'requests':requests})

def become_patient(request):
    if request.method=="POST":   
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']
        phone = request.POST['phone']
        division = request.POST['division']
        dist = request.POST['dist']
        address = request.POST['address']
        gender = request.POST['gender']
        date_of_birth=request.POST['date_of_birth']
        blood_group = request.POST['blood_group']
        disease=request.POST['disease']
        
        if password != confirm_password:
            return redirect('/signup')
        
        print(disease)
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
        patients=Patient.objects.create(patient=user, phone=phone, date_of_birth=date_of_birth, division=division, dist=dist, address=address, blood_group=BloodGroup.objects.get(name=blood_group), disease=disease, gender=gender)
        user.save()
        patients.save()
        messages.success(request, 'Sign-up successful! You can now log in.')
        return redirect('/patient_login')

    return render(request, "become_patient.html")

def become_donor(request):
    if request.method=="POST":   
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        gender = request.POST['gender']
        blood_group = request.POST['blood_group']
        date = request.POST['date']
        image = request.FILES['image']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            # messages.error(request, "Passwords do not match.")
            return redirect('/signup')

        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
        donors = Donor.objects.create(donor=user, phone=phone, state=state, city=city, address=address, gender=gender, blood_group=BloodGroup.objects.get(name=blood_group), date_of_birth=date,image=image)
        user.save()
        donors.save()
        messages.success(request, 'Sign-up successful! You can now log in.')
        return redirect('/donor_login')
    
    return render(request, "become_donor.html")

def Donor_Login(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/donor_view")
        else:
            messages.success(request, 'invalid Password or Username')
            return redirect( "/donor_login")
    return render(request, "donor_login.html")


def Patient_Login(request):
   
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/patient_view")
        else:
            messages.success(request, 'invalid Password or Username')
            return redirect( "/patient_login")
    return render(request, "patient_login.html")

def Logout(request):
    logout(request)
    return redirect('/')

def Donor_view(request):
    try:
        donor = Donor.objects.get(donor=request.user)
        return render(request, 'donor_view.html')
    
    except Donor.DoesNotExist:
        messages.success(request, 'Donor profile does not exist !')
        return redirect('/donor_login') 
    
def Patient_view(request):
    try:
        all_group = BloodGroup.objects.annotate(total=Count('donor'))
        patient = Patient.objects.get(patient=request.user)
        return render(request,"patient_view.html",{'all_group': all_group})
    
    except Patient.DoesNotExist:
        messages.success(request, 'Patient profile does not exist !')
        return redirect('/patient_login')
   
@login_required(login_url = '/donor_login')
def Donor_profile(request):
    donor_profile = Donor.objects.get(donor=request.user)
    return render(request, "donor_profile.html", {'donor_profile':donor_profile})

def Patient_profile(request):
    patient_profile = Patient.objects.get(patient=request.user)
    return render(request, "patient_profile.html", {'patient_profile':patient_profile})

@login_required(login_url = '/login')
def donor_edit_profile(request):
    donor_profile = Donor.objects.get(donor=request.user)
    if request.method == "POST":
        email = request.POST['email']
        phone = request.POST['phone']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        last_donate = request.POST['last_donate']
        image = request.FILES['image']

        donor_profile.donor.email = email
        donor_profile.phone = phone
        donor_profile.state = state
        donor_profile.city = city
        donor_profile.address = address
        donor_profile.last_donate = last_donate
        donor_profile.image = image
        donor_profile.save()
        donor_profile.donor.save()

        # try:
        #     image = request.FILES['image']
        #     donor_profile.image = image
        #     donor_profile.save()
        # except:
        #     pass
        alert = True
        return render(request, "donor_edit_profile.html", {'alert':alert})
    return render(request, "donor_edit_profile.html", {'donor_profile':donor_profile})

def patient_edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user.patient)
        if form.is_valid():
            form.save()
            return redirect('patient_profile')  # Change 'profile' to the URL of your profile page
    else:
        form = EditProfileForm(instance=request.user.patient)

    return render(request, 'patient_edit_profile.html', {'form': form})


@login_required(login_url = '/donor_login')
def change_status(request):
    donor_profile = Donor.objects.get(donor=request.user)
    if donor_profile.ready_to_donate:
        donor_profile.ready_to_donate = False
        donor_profile.save()
    else:
        donor_profile.ready_to_donate = True
        donor_profile.save()
    return redirect('/donor_profile')

def donate_blood(request):
    user = request.user
    full_name = f"{user.first_name} {user.last_name}"

    if request.method == "POST":
        phone = request.POST['phone']
        address = request.POST['address']
        blood_group = request.POST['blood_group']
        date = request.POST['date']
        donate_blood = Donate_Blood.objects.create(donor_id = request.user.id ,name=full_name, phone=phone, address=address, blood_group=BloodGroup.objects.get(name=blood_group), date=date)
        donate_blood.save()
        
        messages.success(request, 'Donation Request Sent Successfully.')
        return redirect("/donor_view")
    
    return render(request, "donate_blood.html")

def donate_history(request):
    requests = Donate_Blood.objects.all()
    user_request = Donate_Blood.objects.filter(donor_id=request.user.id)
    
    if request.user.is_superuser:
        return render(request, "donate_history.html", {'requests':requests})
    else:
        return render(request, "donate_history.html", {'requests':user_request})

def about_us(request):
   return render(request,"about.html")



