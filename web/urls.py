from django.conf.urls import url
from django.urls import path , include
from . import views

urlpatterns=[
path('submit/expense/',views.submit_expense,name='submit_expense'),
]
