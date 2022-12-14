from multiprocessing.dummy import Manager
from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)



#Usuarios
class User(AbstractUser):
    
    #nameUsr = models.CharField(max_length=200)
    genderUsr = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    birthUsr = models.DateField(null=True)
    telUsr= models.CharField(max_length = 9)
    imgUsr = models.ImageField(null=True, blank=True, upload_to="images/")
    ubiUsr = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('user-list', args=[self.pk])

#class Usuarios(models.Model):
#    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #nameUsr = models.CharField(max_length=200)
#    passUsr = models.CharField(max_length=200)
#    ubiUsr = models.CharField(max_length=200)
#    mailUsr = models.EmailField(max_length=254)
    #phoneUsr = models.CharField(max_length=12)
    #pub_date = models.DateTimeField('date published')

#    def __str__(self):
#        return self.user.first_name

#GENDER=[("M"),("F")]
#GENDER_CHOICES = [
#    ('Male', 'Male'),
#    ('Female', 'Female'),
#]

#class Gender(models.TextChoices):
#    Man =   "MAN",("Man")
#    Woman   =   "WOMAN",("WOMAN")

#gender = models.CharField(
#    max_length = 7,
#    choices=Gender.choices,
#    default=Gender.MAN,
#)

class Mascotas(models.Model):
    namePet = models.CharField(max_length=200)
    infoPet = models.CharField(max_length=200)
    agePet = models.DateField(blank=True, null=True)
    typePet = models.CharField(max_length=200)
    imgPet = models.ImageField(null=True, blank=True, upload_to="images/")
    #imgPet = models.FileField(upload_to=None)
    #imgPet = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    genderPet = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    usrPet = models.ForeignKey("User", on_delete=models.CASCADE, null=True)
    #imgPet = models.BooleanField()
    #models.PositiveBigIntegerField()
    
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #genderPet = models.CharField(max_length=1, choices=GENDER)

    def __str__(self):
        return self.namePet
    def get_absolute_url(self):
        return reverse('ilmp:mascotas-list')

class Perdidos(models.Model):
    infoLost = models.CharField(max_length=200)
    dateLost = models.DateTimeField(blank=True, null=True)
    petLost = models.ForeignKey("Mascotas", on_delete=models.CASCADE, null=True)
    ubiLost = models.CharField(max_length=200, blank=True)
    #imgLost = models.ForeignKey("Mascotas", on_delete=models.CASCADE, null=True)
    #ubiLost = models.CharField(max_length=200)
    #typeLost = models.ForeignKey("Mascotas", on_delete=models.CASCADE, null=True)
    #genderLost = models.ForeignKey("Usuarios", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.infoLost
    
class Encuentros(models.Model):
    typeFind = models.CharField(max_length=200)
    imgFind = models.ImageField(null=True, blank=True, upload_to="images/")
    #genderFind = models.CharField(max_length=1, choices=GENDER)
    infoFind = models.CharField(max_length=200)
    genderFind = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    ubiFind = models.CharField(max_length=200, blank=True)
    #ubiFind  = models.CharField(max_length=200)

    def __str__(self):
        return self.typeFind

#class Area(models.Model):
#    country = models.CharField(max_length=200)
#    comunidadautonoma = models.CharField(max_length=200)
#    provincia = models.CharField(max_length=200)
#    calle = models.CharField(max_length=200)

    #def __str__(self):
        #return self.encuentros_text


