from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from purchaser.models import Purchaser,Address
from .models import *
from django.forms.models import model_to_dict
# Create your views here.
def createRed(request,user):
    context = {
        'user': Purchaser.objects.get(pk = user)
    }
    return render(request,'red_page.html',context)
def saveRed(request,user):
    if request.method == "POST":
        data = request.POST['data']
        data = json.loads(data)
        try:
            purchaser = Purchaser.objects.get(pk = data['user'])
            t = purchaser.transaction_set.create(transaction_type = Transaction_Type.objects.filter(name='red').first())
            for item in data['items']:
                itm = Item(name=item['name'],unit_price=item['unit-price'])
                itm.save()
                t.transaction_red_set.create(item=itm,qty=item['qty'])
            return JsonResponse({'status_code':200,'msg':'Transaction has been created'})    
        except:
            return JsonResponse({'status_code':404,'msg':'There was an error, Please try again later'})
def viewRed(request,user,id):
    try:       
        if request.method == 'POST':
            transaction = Transaction.objects.get(pk = id)
            transaction_reds = transaction.transaction_red_set.all()
            items = list()
            print('PUtang')
            for red in transaction_reds:
                item = Item.objects.get(pk = red.item_id)
                item = model_to_dict(item)
                item['qty'] = red.qty
                items.append(item)
        return JsonResponse({'status':200,'items':items})
    except:
        return JsonResponse({'status':500,'msg':'There was an unexpected error, please try again later!'})
    
def createGreen(request,user):
    context = {
        'user': Purchaser.objects.get(pk = user)
    }
    return render(request,'green_page.html',context)
def saveGreen(request,user):
    if request.method == "POST":
        purchaser = Purchaser.objects.get(pk = user)
        t = purchaser.transaction_set.create(transaction_type = Transaction_Type.objects.filter(name='green').first())
        t.transaction_green_set.create(amount = int(request.POST['amount']))
        return JsonResponse({'status_code':200,'msg':'Transaction has been created'})
        try:
            purchaser = Purchaser.objects.get(pk = user)
            t = purchaser.transaction_set.create(transaction_type = Transaction_Type.objects.filter(name='green').first())
            t.transaction_green_set.create(amout = int(request.POST['amount']))
            return JsonResponse({'status_code':200,'msg':'Transaction has been created'})    
        except:
            return JsonResponse({'status_code':404,'msg':'There was an error, please try again later'})
def viewGreen(request,user,id):
    try:
        if request.method == 'POST':
            transaction = Transaction.objects.get(pk = id)
            transaction_green = transaction.transaction_green_set.first()
            return JsonResponse({'status':200,'amount':transaction_green.amount,'date':transaction.created_date.strftime("%Y-%m-%d %H:%M:%S")})
    except:
        return JsonResponse({'status':500,'msg':'There was an unexpected error, please try again later!'})
    
