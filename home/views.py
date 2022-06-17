from django.shortcuts import render,redirect
from datetime import datetime
from home.models import Contact, Gallery, Notice, Stories,Pdf,Result
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


# Create your views here.


def index(request):
    stories=Stories.objects.all()
    notices=Notice.objects.all()
    params={'story':stories,'notice':notices}
    return render(request, 'index.html',params)


def about(request):
    return render(request, 'about.html')

def neet(request):
    return render(request, 'neet.html')

def jee(request):
    return render(request, 'jee.html')

def mhcet(request):
    return render(request, 'mhcet.html')

def sschsc(request):
    return render(request, 'ssc&hsc.html')

def download(request):
    pdf=Pdf.objects.all()
    prams={'pdf':pdf}
    return render(request, 'download.html',prams)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('Select')
        descself = request.POST.get('descself')
        desc = request.POST.get('desc')
        student=request.POST.get('Check1')
        if student=='on':
            student=True
        else:
            student=False

        teacher=request.POST.get('Check2')
        if teacher=='on':
            teacher=True
        else:
            teacher=False
       
        contact=Contact(name=name,email=email,phone=phone,query=query, descself=descself,desc=desc,teacher=teacher,student=student,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        return redirect("/")
    return render(request,'contact.html')

def success(request):
    stories=Stories.objects.all()
    params={'story':stories}
    return render(request,'success.html',params)

def gallery(request):
    gallery=Gallery.objects.all()
    params={'gallery':gallery}
    return render(request,'gallery.html',params)

def result(request):
    result=Result.objects.all()
    params={'result':result}
    return render(request,'result.html',params)


def viewpdf(request, id):
    print("pdf:",id)
    pdf=Pdf.objects.get(id=id)
    print("pdf",type(pdf))
    fs = FileSystemStorage()
    filename = str(pdf.pdf)
    with fs.open(filename) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename[19:]) #user will be prompted with the browser’s open/save file
        #response['Content-Disposition'] = 'inline; filename="mypdf.pdf"' #user will be prompted display the PDF in the browser
        return response

def noticepdf(request, id):
    print("pdf:",id)
    pdf=Notice.objects.get(id=id)
    print("pdf:", type(pdf))
    fs = FileSystemStorage()
    filename = str(pdf.pdf)
    with fs.open(filename) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename[11:]) #user will be prompted with the browser’s open/save file
        #response['Content-Disposition'] = 'inline; filename="mypdf.pdf"' #user will be prompted display the PDF in the browser
        return response

def notice(request,id):
    note=Notice.objects.get(id=id)
    notes=Notice.objects.all()
    print("note",note)
    prams={'notice':note,'notices':notes}
    print("dic",prams)
    return render(request,'notice.html',prams)