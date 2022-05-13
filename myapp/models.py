from django.db import models


# Create your models here.


class User(models.Model):
    
    ROLES = (

        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patiences', 'Patience'),

    )


    roles = models.CharField(max_length=30,choices = ROLES)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    address = models.TextField(default=None,blank=True,null=True)
    gender = models.CharField(max_length=6)
    speciality = models.CharField(max_length=30,default=None,blank=True,null=True)
    clinic_name=models.CharField(max_length=30,default=None,blank=True,null=True)
    profile = models.ImageField(upload_to='profiles/',blank=True,null=True)
    
    

    def __str__(self):
        return self.name
        
class Slot(models.Model):
    TIMESLOT_LIST = (
        (0, '09:00 am To 10:00 am'),
        (1,'10:00 am TO 11:00 am'),
        (2, '11:00 am To 12:00 am'),
        (3, '12:00 am To 01:00 pm'),
        (4, '02:00 pm To 03:00 pm'),
        (5, '03:00 pm To 04:00 pm'),
        (6, '04:00 pm To 05:00 pm'),
    )
    WEEKS = (
        (0,'Monday'),
        (1,'Tuesday'),
        (2,'Wednesday'),
        (3,'Thursday'),
        (4,'Friday'),
        (5,'Saturday'),
        (6,'Sunday'),
    )
    doctor_id = models.ForeignKey(User,on_delete=models.CASCADE)
    weeks  = models.IntegerField(choices=WEEKS)
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)
    slotsize=models.IntegerField(default=1)



    def __int__(self):
        return self.doctor_id

class Appointment(models.Model):
    STATUS = (
        (0,'pending'),
        (1,'Completed'),
        (2,'Absent'),
        (3,'Canceled'),
    ) 
    slot = models.ForeignKey(Slot,on_delete=models.CASCADE,null=True,blank=True)  
    name =  models.CharField(max_length=30)
    phone = models.IntegerField(null=True,blank=True)
    weeks = models.IntegerField(null=True,blank=True)
    timeslot = models.IntegerField(null=True,blank=True)
    description = models.TextField(default=None,null=True,blank=True)
    status = models.IntegerField(default=0,choices=STATUS)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    
    # def __str__(self):
    #     return self.description

