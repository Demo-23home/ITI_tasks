from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Instructor 
# Create your views here.




def list(request):
    inst = Instructor.objects.all()


    return render(request,'instructor/list.html',{'inst':inst,})



def instert(request):
    return render(request,'instructor/insert.html')



def update(request):
    return render(request,'instructor/update.html')



def delete(request):
    return render(request,'instructor/delete.html')



# views.py (inside your app)
 # Import your Instructor model

def register(request):
    if request.method == 'POST':
        # Get form data from the request
        usrnme = request.POST.get('usrnme')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        track = request.POST.get('track')
        passwd = request.POST.get('passwd')

        # Create a new Instructor object and save it to the database
        instructor = Instructor(usrnme=usrnme, f_name=f_name, l_name=l_name, email=email, track=track, passwd=passwd)
        instructor.save()

        # Redirect to a success page or login page
        return redirect('list')  # Replace 'success_page' with the URL name of your success page

    return render(request, 'instructor/register.html')
