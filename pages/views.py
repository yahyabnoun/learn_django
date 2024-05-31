from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,"pages/index.html",{"name":"yahya bnoun" , "filesize" :106398})

def aboutPage(request):
    return render(request,"pages/about.html")

def fromPage(request):
    print(request.POST.get("email"))


    return render(request,"pages/form.html")