from pdb import post_mortem
from django.shortcuts import render

from app.models import *
from django.http import HttpResponse

# Create your views here.

def Insert_School(request):

    if request.method=='POST':

        scn=request.POST['scn']
        sp=request.POST['sp']
        sl=request.POST['sl']
        
        SO=School.objects.get_or_create(ScName=scn,ScPrincipal=sp,ScLocation=sl)[0]
        SO.save()
        QLSO=School.objects.all()
        d={'QLSO':QLSO}
        return render(request,'display_School.html',d)
    
    return render(request,'Insert_School.html')



def Insert_Student(request):

    if request.method=='POST':

        scn=request.POST['scn']
        sn=request.POST['sn']
        si=request.POST['si']

        SO=School.objects.get(ScName=scn)

        STO=Student.objects.get_or_create(ScName=SO,SName=sn,Sid=si)[0]
        STO.save()

        QSTO=Student.objects.all()
        
        d={'QSTO':QSTO}

        return render(request,'display_Student.html',d)

    return render(request,'Insert_Student.html')
