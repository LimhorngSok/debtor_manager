from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Purchaser,Address 
from transaction.models import *
from django.contrib import messages
from django.forms.models import model_to_dict
# Create your views here.
def create(request):
    return render(request,'create-purchaser.html')
def save(request):
    if request.method == 'POST':
        address = Address.objects.get_or_create(name=request.POST['address'])
        address[0].purchaser_set.create(name=request.POST['name'],phone=request.POST['phone'])
        messages.success(request,'Purchaser has been created')
        return redirect('/purchaser/create',kwargs={ 'msg': 'Purchaser has been created' })
def detail(request,id):
    if request.method == 'POST':
        purchaser = Purchaser.objects.get(pk = id)
        transactions = purchaser.transaction_set.all().order_by('-created_date').values('id','transaction_type_id','created_date')
        return JsonResponse({'status_code':200,'purchaser':model_to_dict(purchaser),'transactions':list(transactions),'totalDept':purchaser.totalDept()},safe=False)
    return id