from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name = 'index'),
    path('about-us', views.about_us, name= 'aboutus'),
    path('contact-us', views.contact_us, name = 'contactus'),
    path('footer', views.footer, name = 'footer' ),
    path('student_dashboard', views.student_dashboarad, name = 'studentdashboard'),
    path('job-list', views.job_list, name = 'joblistpost'),
    path('company-dashboard', views.company_dashboard, name = 'companydashboard'),
    path('student-signup', views.student_sighup, name = 'studentsignup'),
    path('student-login', views.student_login, name = 'studentlogin')


]