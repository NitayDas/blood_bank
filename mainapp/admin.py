from django.contrib import admin
from . models import *

admin.site.register(RequestBlood)
admin.site.register(BloodGroup)
admin.site.register(Donor)
admin.site.register(Patient)
admin.site.register(Donate_Blood)