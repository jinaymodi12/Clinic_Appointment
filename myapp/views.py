from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from.models import*
from django.db.models import Q


# Create your views here.
#<<<<<<<<<<<<<<<<<<<<<<<< Admin >>>>>>>>>>>>>>>>>>>>>>#
def indexx(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        return render(request,'index.html',{'uid':uid})
    return redirect('login')

def signupp(request):
    return render(request,'sign-up.html')

def logoutt(request):
    del request.session['email']
    return redirect('login')

def index_doc(request):
    if 'email' in request.session:
     uid = User.objects.get(email = request.session['email'])
     return render(request,'index-doctor.html',{'uid':uid})

    return redirect('login')

def index_patiences(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        return render(request,'index-patience.html',{'uid':uid})
    return redirect('login')

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
    if 'email' in request.session:
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
    return redirect('login')

     #<<<<<<<<<<<<<<<<<<<<<< Doctor >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

def view_doctor(request):
    if 'email' in request.session:
        a=User.objects.all().filter(roles ='doctor')
        return render(request,'list_doctor.html',{'a':a})
    return redirect('login')

def updates_doctor(request,pk):
    if 'email' in request.session:
        uid = User.objects.get(id=pk)
        if request.method == 'POST':
            uid.name=request.POST['name']
            uid.email=request.POST['email']
            uid.password=request.POST['password']
            uid.save() 
            return render(request,'update_doctor.html',{'uid':uid,'msg':'Profile Updated Successfully!!'})
        else:
            return render(request,'update_doctor.html',{'uid':uid})
    return redirect('login')
   



def deletes_doctor(request,pk):
    if 'email' in request.session:
        uid = User.objects.get(id=pk)
        uid.delete()
        return redirect('list_doctor')
    return redirect('login')

def updates_profile(request):
    if 'email' in request.session:
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
    return redirect('login')

def appointment_views(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email']) 
        many=Appointment.objects.all()
        return render(request,'appointment-view.html',{'many':many,'uid':uid})
    return redirect('login')
    
def patiences_create(request):
    if 'email' in request.session:
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
                # gender  = request.POST['gender'],
                profile = request.FILES['profile']
            )
                return render(request,'create_patience.html',{'msg':'Patience Create Successfully!!'})
        else:
            return render(request,'create_patience.html')
    return redirect('login')


def view_patience(request):
    if 'email' in request.session:
        many=User.objects.all().filter(roles='patiences')
        return render(request,'list_patience.html',{'many':many})
    return redirect('login') 

def deletes_patience(request,pk):
    if 'email' in request.session:
        uid=User.objects.get(id=pk)
        uid.delete()
        return redirect('list_patience')
    return redirect('login')


def updates_patience(request,pk):
    if 'email' in request.session:
        uid = User.objects.get(id=pk)
        if request.method == 'POST':
            uid.name=request.POST['name']
            uid.email=request.POST['email']
            uid.password=request.POST['password']
            uid.save()
            return redirect('list_patience')
        else:
            return render(request,'update_patience.html',{'uid':uid})
    return redirect('login')

def appointment_status(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        many = Appointment.objects.filter(name=uid)

        print(many)
        return render(request,'appointment-status.html',{'many':many,'uid':uid})
    return redirect('login')



#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Slot >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

def slot_add(request):
    if 'email' in request.session:
        uid=Slot.objects.all()
        doctor=User.objects.get(email=request.session['email'])
        # uid=Slot.objects.filter(doctor_name=doctor)
        if request.method=='POST':
         
            Slot.objects.create(
            doctor_id = doctor,
            weeks = request.POST['weeks'],
            timeslot = request.POST['timeslot'],
            )
            return render(request,'slot.html',{'uid':uid,'msg':'Slot Added Successfully!'})
        else:
            return render(request,'slot.html',{'uid':uid})
    return redirect('login')

def view_slots(request):
    if 'email' in request.session:
        doc = User.objects.get(email=request.session['email'])
        many = Slot.objects.all().order_by('weeks')
        return render(request,'view-slot.html',{'many':many,'doc':doc})
    return redirect('login')

def update_slots(request,pk):
    if 'email' in request.session:
        id=Slot.objects.get(id=pk)
        if request.method == 'POST':
            id.weeks=request.POST['weeks']
            id.timeslot=request.POST['timeslot']
            id.save()
            return redirect('view-slot')
        else:
            return render(request,'update-slot.html',{'id':id})
    return redirect('login')

def delete_slots(request,pk):
    if 'email' in request.session:
        id=Slot.objects.get(id=pk)
        id.delete()
        return redirect('view-slot')
    return redirect('login')




def profile_patience(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        if request.method == 'POST':
            uid.name=request.POST['name']
            # uid.email=request.POST['email']
            uid.password=request.POST['password']
            uid.gender=request.POST['gender']
            uid.profile=request.FILES['profile']
            uid.save()
            return redirect('index_patience')
        else:
            return render(request,'patience-edit.html',{'uid':uid})
    return redirect('login')

def doctor_view(request):
    user=User.objects.filter(roles='doctor')
    return render(request,'doctor-view.html',{'user':user})
def available_slot(request,pk):
    user=User.objects.get(id=pk)
    slot=Slot.objects.filter(doctor_id = user)
    return render(request,'slot-detail.html',{'user':user,'slot':slot})




#<<<<<<<<<<<<<<<<<<<<<<<<<<<< Appointment >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
def appointments_form(request,pk):
    if 'email' in request.session:
        user=User.objects.get(email=request.session['email'])
        data=Slot.objects.get(id=pk)
        print(data)
       
        if request.method =='POST':
            data.slotsize-=1
            data.save()

            Appointment.objects.create(
            name=request.POST['name'],
            user=user,
            description = request.POST['description'],
            )
            return render(request,'appointment-form.html',{'msg':'Appointment Send To Doctor Successfully!!','user':user,'data':data})
        else:
            return render(request,'appointment-form.html',{'user':user,'data':data})
    return redirect('login')



#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< status >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

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


