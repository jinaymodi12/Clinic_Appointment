from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #<<<<<<<<<<<<<<<<<<<<< Admin >>>>>>>>>>>>#
    path('index',views.indexx,name='index'),
    path('signup/',views.signupp,name='signup'),
    path('logout/',views.logoutt,name='logout'),
    path('indexdoc/',views.index_doc,name='index_doc'),
    path('',views.logins,name='login'),
    path('doctorcreate/',views.doctor_create,name='create_doctor'),
    path('viewdoctor/',views.view_doctor,name='list_doctor'),
    path('indexpatience/',views.index_patiences,name='index_patience'),

    path('profile/',views.updates_profile,name='update_profiles'),
#<<<<<<<<<<<<<<<<<<< doctor >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
    path('updatedoctor/<int:pk>',views.updates_doctor,name='update_doctor'),
    path('deletedoctor/<int:pk>',views.deletes_doctor,name='delete_doctor'),
    path('patiencecreate/',views.patiences_create,name='patience_create'),
    path('viewdpatience/',views.view_patience,name='list_patience'),
    path('deletepatience/<int:pk>',views.deletes_patience,name='delete_patience'),
    path('updatepatience/<int:pk>',views.updates_patience,name='update_patience'),
    path('appointmentget',views.appointment_views,name='appointment-views'),
#<<<<<<<<<<<<<<<<<<<<<<<<<  slot  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
    path('slotadd/',views.slot_add,name='slots'),
    path('viewslot/',views.view_slots,name='view-slot'),
    path('updateslot/<int:pk>',views.update_slots,name='update-views'),
    path('deleteslot/<int:pk>',views.delete_slots,name='delete-views'),

#<<<<<<<<<<<<<<<<<<<<<<<<<< patience >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
    path('patienceedit/',views.profile_patience,name='patience-edit'),
    path('doctorview/',views.doctor_view,name='doctor-view'),
    path('availableslot/<int:pk>',views.available_slot,name='slot-detail'),
    path('appointmentform/<int:pk>',views.appointments_form,name='appointment-form'),
    path('appointmentstatus/',views.appointment_status,name='appointment-status'),

#<<<<<<<<<<<<<<<<<<<<<<<<<<<< status >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
    path('completestatus/<int:pk>',views.complete_status,name='complete-status'),
    path('absentstatus/<int:pk>',views.absent_status,name='absent-status'),
    path('cancelstatus/<int:pk>',views.cancel_status,name='cancel-status'),
    
    



    



    
    




    
]
