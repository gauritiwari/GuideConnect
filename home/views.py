from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def login(request):
    return render(request,'login.html')
def guide(request):
    return render(request,'guide.html')
def tourist(request):
    return render(request,'tourist.html')

