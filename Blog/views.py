from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

def banormus(request):
    return render(request , 'banormus.html' )

def band(request):
    if request.method ==  "GET":
        return render(request , 'band.html' )
    if request.method ==  "POST":
        genrejadid = request.POST['Genre']
        instrumentjadid = request.POST['Instrument']
        namejadid= request.POST['name']
        emailjadid= request.POST['email']
        nationalityjadid= request.POST['country']
        Band.objects.create(bgenre=genrejadid,binstrument=instrumentjadid,bname=namejadid,
        bemail=emailjadid,bnationality=nationalityjadid)
        b = Musician.objects.filter(mgenre=genrejadid,minstrument=instrumentjadid)
        output = { 'band' : b }
        return render(request , 'connectb.html' , context = output ) 
        
def musician(request):
    if request.method ==  "GET":
        return render(request , 'musician.html' )
    elif request.method ==  "POST":
        genrejadid = request.POST['Genre']
        instrumentjadid = request.POST['Instrument']
        namejadid= request.POST['name']
        emailjadid= request.POST['email']
        nationalityjadid= request.POST['country']
        Musician.objects.create(mgenre=genrejadid,minstrument=instrumentjadid,mname=namejadid,
        memail=emailjadid,mnationality=nationalityjadid)
        b = Band.objects.filter(bgenre=genrejadid,binstrument=instrumentjadid)
        output = { 'musician' : b }
        return render(request , 'connectm.html' ,  context = output )

