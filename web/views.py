from django.shortcuts import render
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from web.models import Token,Expence,Income,User
from datetime import datetime
# Create your views here.
@csrf_exempt


def submit_expense(request):
    now=datetime.now()
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token ).get()
    Expence.objects.create(text=request.POST['text'],user=this_user
    ,amount=request.POST['amount'],date=now)
    """user submit an  expense"""
    print("we are here")
    print(request.POST)
    return JsonResponse({
    "status":"ok"},
    encoder=JSONEncoder)
