from django.db import models
from django.contrib.auth.models import User

class BloodGroup(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class RequestBlood(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=300, blank=True)
    address = models.CharField(max_length=500, blank=True)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    date = models.CharField(max_length=100, blank=True)
    status=models.IntegerField(default=0)
    # state = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Donate_Blood(models.Model):
    donor_id = models.IntegerField(default = 0 )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=500, blank=True)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    date = models.CharField(max_length=100, blank=True)
    status=models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Patient(models.Model):
    patient = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    date_of_birth = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    division = models.CharField(max_length=100)
    dist = models.CharField(max_length=100)
    address = models.TextField(max_length=500, default="")
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    disease=models.CharField(max_length=200)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.patient.username

class Donor(models.Model):
    donor = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    date_of_birth = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.TextField(max_length=500, default="")
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    last_donate = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    ready_to_donate = models.BooleanField(default=True)

    def __str__(self):
        return str(self.blood_group)