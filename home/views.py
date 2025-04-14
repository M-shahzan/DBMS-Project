from django.shortcuts import render,HttpResponse
from .models import restables
from menu.models import Menu
# Create your views here.

def index(request):
    count = restables.objects.count()
    available = restables.objects.filter(status = 'available').count()
    reserved = restables.objects.filter(status = 'reserved').count()
    item_count = Menu.objects.count()
    details = {
        'menu_count':item_count,
        'count':count,
        'available':available,
        'reserved':reserved,
    }
    return render(request,'home.html',{'details' : details })