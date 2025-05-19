from django.shortcuts import render
from .models import FbModel
from .forms import FbForm
def home(request):
    if request.method=="POST":
        na=request.POST.get("name")
        cl = request.POST.get("Class")
        fb = request.POST.get("feedback")
        data=FbModel(name=na,Class=cl,feedback=fb)
        data.save()
        fm=FbForm()
        return render(request,"home.html",{"fm":fm,"msg":"Thanks for your feedback"})
    else:
        fm=FbForm()
        return render(request,"home.html",{"fm":fm})
# Create your views here.
