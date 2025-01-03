from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def upload_file(request: HttpRequest) -> HttpResponse:
    raise NotImplementedError