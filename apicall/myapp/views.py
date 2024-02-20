
from rest_framework.decorators import api_view
import requests
from django.http import JsonResponse
import json



@api_view(['GET'])
def users(request):
    response = requests.get('https://randomuser.me/api/')
    #convert reponse data into json
    users = response.json()
    print(users)
    return JsonResponse(users, status=200)



@api_view(['GET'])
def quote(request, page_number):
    response = requests.get('https://quotable.io/quotes?page={page_number}')
    return JsonResponse(json.dumps(response.json()), safe=False,status=200)


