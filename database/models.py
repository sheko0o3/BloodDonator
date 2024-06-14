from django.db import models


from django.contrib.auth.models import User


class Gender(models.TextChoices):
    Male = "Male"
    Female = "Female"


class BloodType(models.Model):
    bloodtype = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.bloodtype


class UserInformation(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    bloodType = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    mobile = models.CharField(max_length=11, null=False, blank=False)
    govern = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=50, null=False, blank=False)
    Card_number = models.CharField(max_length=14, null=False, blank=False)
    date_of_donation = models.DateTimeField(null=True, blank=True)
    age = models.IntegerField(null=False, blank=False)
    gender = models.CharField(max_length=20, choices=Gender.choices, null=False, blank=False)
    
    

    def __str__(self) -> str:
        return self.user.username


class Govern(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    


class GovernStates(models.Model):
    govername = models.ForeignKey(to=Govern, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
    

class Donation(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_of_donation = models.DateField()
