from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. 

# function-based views

def create_book(request):

    #get the request body
    my_body=request.body()

    #deserialize (turn from json to an oop object)
    
    #save to db

    #return a JSON response showing if it succeeded or failed

    pass

def get_all_books(request):
    pass


