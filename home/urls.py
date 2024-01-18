from django.urls import path
from . import views
#app_name = 'home_patient'

urlpatterns = [
    path("", views.index, name="index"),
    
    path("donors_list/<int:myid>/", views.donors_list, name="donors_list"),
    
    path("donors_details/<int:myid>/", views.donors_details, name="donors_details"),
    
    path("request_blood/", views.request_blood, name="request_blood"),
    
    path("see_all_request/", views.see_all_request, name="see_all_request"),
    
    path("become_donor/", views.become_donor, name="become_donor"),
    
    path("become_patient/", views.become_patient, name="become_patient"),
    
    path("donor_login/", views.Donor_Login, name="donor_login"),
    
    path("patient_login/", views.Patient_Login, name="patient_login"),
    
    path("logout/", views.Logout, name="logout"),
    
    path('patient_view/', views.Patient_view, name='patient_view'),
     
    path('donor_view/', views.Donor_view, name='donor_view'),
    
    path('donor_profile/', views.Donor_profile, name='donor_profile'),
    
    path('patient_profile/', views.Patient_profile, name='patient_profile'),
    
    path('donor_edit_profile/', views.donor_edit_profile, name='donor_edit_profile'),
    
    path('patient_edit_profile/', views.patient_edit_profile, name='patient_edit_profile'),
    
    path('change_status/', views.change_status, name='change_status'),
    
    path('donate_blood/', views.donate_blood, name='donate_blood'),
    
    path('donate_history/', views.donate_history, name='donate_history'),
    
    path('about_us/', views.about_us, name='about_us'),
           
]