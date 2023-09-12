from django.shortcuts import render,redirect
from .models import Traniee
# Create your views here.


def traniee_list(request):
    tran = Traniee.objects.all()


    return render(request,'traniee/list.html',{'tran':tran,})




def instert(request):
    return render(request,'traniee/insert.html')



def update(request):
    return render(request,'traniee/update.html')



def delete(request):
    return render(request,'traniee/delete.html')





def Trainee_register(request):
    if request.method == 'POST':
        usrnme = request.POST.get('usrnme')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        track = request.POST.get('track')
        passwd = request.POST.get('passwd')

        traniee = Traniee(usrnme=usrnme, f_name=f_name, l_name=l_name, email=email, track=track, passwd=passwd)
        traniee.save()

        return redirect('listTraniee')  

    return render(request, 'traniee/register.html')