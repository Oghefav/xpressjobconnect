from django.shortcuts import render,redirect
from .forms import StudentLogin,StudentSignup

# Create your views here.
def landing_page(request):
    return render(request, 'landing_page.html')

def about_us(request):
    return render(request, 'about_us.html')  

def contact_us(request):
    return render(request, 'contact_us.html')

def footer(request):
    return render(request, 'footer.html')

def student_dashboarad(request):
    return render(request, 'dashboard/student_dashboard.html')

def job_list(request):
    return render(request, 'job/job_list.html')

def company_dashboard(request):
    return render(request, 'dashboard/companydashboard') 

def student_login(request):
    if request.method == 'POST':
        form = StudentLogin(request.POST)
        if form.is_valid():
            if user is not none:
               return redirect('index')
        else:
            form = StudentLogin()
                
    return render(request, 'auth/student_login.html')

# def student_sighup(request):
#     if request.method == 'POST':
#         form = StudentSignup(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('student_login')
#     else:
#         form = StudentSignup()
    
#     return render(request, auth/student_signup.html', {'form' : form})

def student_sighup(request):
    try:
        if request.method == 'POST':
            user_form = StudentSignup(request.POST)
            if user_form.is_valid():
                # Create a new user object but avoi
                print(user_form)
                new_user = user_form.save(commit=False)
                # Set the chosen password
                new_user.set_password(user_form.cleaned_data['password2'])
                # Save the User object
                new_user.save()
                return redirect("studentlogin")
            return redirect("studentsignup")
        else:
            user_form = StudentSignup()
            return render(request, 'auth/student_signup.html', {'user_form': user_form})



    except Exception as e:
        print(e)
    