from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# function-based views
def get_books(request):
    return HttpResponse("Here are the books ")

def get_authors(request):
    return HttpResponse("Here are the authors ")

def login(request):
    # get json body using deserializer
    # get username from the body
    # get password from the body
    # hash password
    # find user from db with that username
    # if user does not exist return a message telling user that the username does not exist
    # else compare password in db vs hashed password
    # if they match authenticate the user
    # else send message saying wrong password
    pass