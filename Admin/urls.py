from django.urls import path
from . import views
#app_name = 'home_patient'

urlpatterns = [ 
    path('patient_blood_request/', views.Patient_blood_request, name='patient_blood_request'),
    
    path('patient_blood_disapprove/<str:request_id>', views.Patient_blood_disapprove, name='patient_blood_disapprove'),
    
    path('patient_blood_approve/<str:request_id>', views.Patient_blood_approve, name='patient_blood_approve'),
    
    path("admin_login/", views.Admin_Login, name="admin_login"),
    
    path("admin_view/", views.Admin_view, name="admin_view"),
    
    path('available_donors/', views.Available_Donors, name='available_donors'),
    
     path('donor_blood_disapprove/<str:request_id>', views.Donor_blood_disapprove, name='donor_blood_disapprove'),
    
    path('donor_blood_approve/<str:request_id>', views.Donor_blood_approve, name='donor_blood_approve'),
    
]
    