from django.shortcuts import render

from travelapp1.models import Place3


# Create your views here.
def travel(request):
    obj = Place3.objects.all()
    print(obj)
    return render(request,"index.html",{'result': obj})