from django.shortcuts import render
from purchaser.models import *
from transaction.models import *
import json
from django.http import JsonResponse




# Create your views here.
def home(request):
    return render(request,'home/index.html')

def search(request):
    if request.method == 'POST':
        data = request.POST['data']
        data = json.loads(data)
       
        address = Address.objects.get(name=data['location'])
        purchasers = address.purchaser_set.filter(name__icontains = data['name'], phone__icontains = data['phone']).values('id','name','phone','address')
        return JsonResponse({'status_code':200,'data':list(purchasers)})
    else:
        return render(request,'home/search.html')
def address(request):
    if request.method == 'POST':
        address = Address.objects.all().values_list('name',flat=True)
        return JsonResponse({'data':list(address)})