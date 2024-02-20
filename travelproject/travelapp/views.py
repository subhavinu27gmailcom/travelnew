from django.shortcuts import render

# Create your views here.
def travel1(request):
    return render(request,"index.html")