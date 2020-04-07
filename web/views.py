from django.shortcuts import render
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from web.models import Token,Expence,Income,User
from datetime import datetime
# Create your views here.
@csrf_exempt

#TODO;user and amount and text might be fake
def submit_expense(request):
    if 'date' in request.POST:
        now=request.POST['date']
    else :
        now=datetime.now()
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token ).get()
    Expence.objects.create(text=request.POST['text'],user=this_user
    ,amount=request.POST['amount'],date=now)
    return JsonResponse({
    "status":"ok"},
    encoder=JSONEncoder)

@csrf_exempt
def submit_income(request):
    if 'date' in request.POST:
        now=request.POST['date']
    else :
        now=datetime.now()
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token ).get()
    Income.objects.create(text=request.POST['text'],user=this_user
    ,amount=request.POST['amount'],date=now)
    return JsonResponse({
    "status":"ok"},
    encoder=JSONEncoder)
