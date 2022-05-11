from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from.models import*

# Create your views here.
def indexx(request):
        uid = User.objects.get(email=request.session['email'])
        return render(request,'index.html',{'uid':uid})

def signupp(request):
    return render(request,'sign-up.html')

def logoutt(request):
    del request.session['email']
    return redirect('login')

def ind(request):
    return render(request,'index1.html')

def index_doc(request):
    uid = User.objects.get(email = request.session['email'])
    return render(request,'index-doctor.html',{'uid':uid})

def index_patiences(request):
    uid = User.objects.get(email = request.session['email'])
    return render(request,'index-patience.html',{'uid':uid})

def logins(request):
    if request.method == 'POST':
                    uid = User.objects.get(email=request.POST['email'])
                    if uid.roles == "admin":
                        if request.POST['password'] == uid.password:
                            request.session['email'] = request.POST['email']
                            print(request.session['email'])
                            return redirect('index')
                        return render(request,'login.html',{'msg':'Please Enter Valid Password'})
                    elif uid.roles == "doctor":
                        if request.POST['password'] == uid.password:
                            request.session['email'] = request.POST['email']
                            print(request.session['email'])
                            return redirect('index_doc')

                        return render(request,'login.html',{'msg':'Please Enter Valid Password'})
                    else:
                        if request.POST['password'] == uid.password:
                            request.session['email'] = request.POST['email']
                            print(request.session['email'])
                            return redirect('index_patience')
                        return render(request,'login.html',{'msg':'Please Enter Valid Password'})
               
                    msg = "Please Enter Valid Email"
                    return render(request,'login.html',{'msg':msg})
    return render(request,'login.html') 

def doctor_create(request):
    if request.method == "POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg = "Doctor Email is already Exits "
            return render(request,'create_doctor.html',{'msg':msg})
        except:
                User.objects.create(
                clinic_name=request.POST['clinic_name'],
                gender = request.POST['gender'],
                speciality=request.POST['speciality'],    
                roles = request.POST['roles'],
                name = request.POST['name'],
                email = request.POST['email'],
                password = request.POST['password'],
            )
                return render(request,'create_doctor.html',{'msg':'Doctor Profile Create Successfully!!'})
    else:
        return render(request,'create_doctor.html')


def view_doctor(request):
    a=User.objects.all().filter(roles ='doctor')
    return render(request,'list_doctor.html',{'a':a})

def updates_doctor(request,pk):
    uid = User.objects.get(id=pk)
    if request.method == 'POST':
        uid.name=request.POST['name']
        uid.email=request.POST['email']
        uid.password=request.POST['password']
        uid.save() 
    return render(request,'update_doctor.html',{'uid':uid,'msg':'Profile Updated Successfully!!'})
   



def deletes_doctor(request,pk):
    uid = User.objects.get(id=pk)
    uid.delete()
    return redirect('list_doctor')

def updates_profile(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.name=request.POST['name']
        uid.email=request.POST['email']
        uid.password=request.POST['password']
        uid.gender=request.POST['gender']
        uid.speciality=request.POST['speciality']
        uid.clinic_name=request.POST['clinic_name']
        uid.save()
        return redirect('index_doc')
    else:
        return render(request,'update-profile.html',{'uid':uid})

def appointment_views(request):
    uid=User.objects.get(email=request.session['email']) 
    many=Appointment.objects.all()
    return render(request,'appointment-view.html',{'many':many})
    
   






def patiences_create(request):
    if request.method == "POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg = "Patience Email is already Exits "
            return render(request,'create_patience.html',{'msg':msg})
        except:
                User.objects.create(
                address=request.POST['address'],
                roles = request.POST['roles'],
                name = request.POST['name'],
                email = request.POST['email'],
                password = request.POST['password'],
            )
                return render(request,'create_patience.html',{'msg':'Patience Create Successfully!!'})
    else:
        return render(request,'create_patience.html')


def view_patience(request):
    many=User.objects.all().filter(roles='patiences')
    return render(request,'list_patience.html',{'many':many}) 

def deletes_patience(request,pk):
    uid=User.objects.get(id=pk)
    uid.delete()
    return redirect('list_patience')

def updates_patience(request,pk):
    uid = User.objects.get(id=pk)
    if request.method == 'POST':
        uid.name=request.POST['name']
        uid.email=request.POST['email']
        uid.password=request.POST['password']
        uid.save()
        return redirect('list_patience')
    else:
        return render(request,'update_patience.html',{'uid':uid})

def appointment_status(request):
    uid=User.objects.get(email=request.session['email'])
    many = Appointment.objects.filter(name=uid)
    print(many)
    return render(request,'appointment-status.html',{'many':many})





def slot_add(request):
    doctor=User.objects.get(email=request.session['email'])
    uid=Slot.objects.all()
    if request.method=='POST':
         
        Slot.objects.create(
        doctor_name = doctor,
        weeks = request.POST['weeks'],
        timeslot = request.POST['timeslot'],
    )
        return render(request,'slot.html',{'msg':'Slot Added Successfully!'})
    else:
    
        return render(request,'slot.html',{'uid':uid})

def view_slots(request):
    doc = User.objects.get(email=request.session['email'])
    many=Slot.objects.all().order_by('weeks')
    return render(request,'view-slot.html',{'many':many})

def update_slots(request,pk):
    id=Slot.objects.get(id=pk)
    if request.method == 'POST':
        id.weeks=request.POST['weeks']
        id.timeslot=request.POST['timeslot']
        id.save()
        return redirect('view-slot')
    else:
        return render(request,'update-slot.html',{'id':id})

def delete_slots(request,pk):
    id=Slot.objects.get(id=pk)
    id.delete()
    return redirect('view-slot')




def profile_patience(request):
    uid=User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.name=request.POST['name']
        uid.email=request.POST['email']
        uid.password=request.POST['password']
        uid.gender=request.POST['gender']
        uid.save()
        return redirect('index_patience')
    else:
        return render(request,'patience-edit.html',{'uid':uid})

def patience_view(request):
    many=User.objects.all().filter(roles='doctor')[::-1]
    return render(request,'patience-view.html',{'many':many})

def appointments(request,pk):
    uid=User.objects.get(email=request.session['email'])
    data=Slot.objects.all()
    return render(request,'appointment.html',{'data':data})

def appointments_form(request,pk):
    user=User.objects.get(email=request.session['email'])
    data=Slot.objects.get(id=pk)
    if request.method =='POST':
        data.slotsize-=1
        data.save()

        Appointment.objects.create(
            name=request.POST['name'],
            # user=user,
            slot=data,
            phone=request.POST['phone'],
            weeks=request.POST['weeks'],
            timeslot=request.POST['timeslot'],
            description = request.POST['description'],
        )
        return render(request,'appointment-form.html',{'msg':'Appointment Send To Doctor Successfully!!','user':user,'data':data})
    else:
        return render(request,'appointment-form.html',{'user':user,'data':data})





def complete_status(request,pk):
    uid = Appointment.objects.get(id=pk)
    uid.status = 1
    uid.save()
    return redirect('appointment-views')

def absent_status(request,pk):
    uid = Appointment.objects.get(id=pk)
    uid.status = 2
    uid.save()
    return redirect('appointment-views')

def cancel_status(request,pk):
    uid = Appointment.objects.get(id=pk)
    uid.status = 3
    uid.save()
    return redirect('appointment-views')


