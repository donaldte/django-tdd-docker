from django.shortcuts import render
from django.http import JsonResponse

def first_view(request):
    context = {
        'ping': 'pong'
    }

    return JsonResponse(context)