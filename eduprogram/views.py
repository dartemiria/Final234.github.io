from django.shortcuts import render

def index(request):
    return render(request, 'eduprogram/me.html')

def aboutme(request):
    return render(request,'eduprogram/aboutme.html')

def edupr(request):
    return render(request,'eduprogram/edupr.html')

def menegerr(request):
    return render(request,'eduprogram/menegerr.html')

def classmate(request):
    return render(request,'eduprogram/classmate.html')


