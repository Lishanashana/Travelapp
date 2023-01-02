# Create your views here.
from django.shortcuts import render

from . models import place
from . models import team


def home(request):
    obj = place.objects.all()
    obj2 = team.objects.all()
    return render(request, "index.html",{'result': obj, 'result2': obj2})


