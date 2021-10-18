from rest_framework.decorators import api_view, renderer_classes
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import json, jwt, random, string, datetime, calendar
from rest_framework.response import Response
from .models import *
from .serializers import *


# @csrf_exempt
@api_view(['GET', 'POST'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def user_authontication(request) :
    if request.method == 'POST' :
        print(request.data)
        email = request.data['login']
        password = request.data['password']
        response = {"a":"b"}
        user_data = Users.objects.all().values().filter(email=email)
        user_data = list(user_data)
        print(user_data[0]['id'])
        if password == user_data[0]['password']:
            future = datetime.datetime.utcnow() + datetime.timedelta(days=1)
            payload = {
                'user_id': user_data[0]['id'],
                'exp': calendar.timegm(future.timetuple())
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
            response = {'token': token}
            return Response(response)
        else:
            response = {'error': 'Invalid data!'}
            return JsonResponse(response)

@csrf_exempt
def get_user_data(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    token = body['token']

    try:
        jwt_data = jwt.decode(token, 'secret', algorithms=['HS256'])
        print("@@@@@@@@@ jwt_data @@@@@@@@@@@", jwt_data)
        user_data = Users.objects.all().values().filter(id=jwt_data['user_id'])
        user_data = list(user_data)
        print(user_data)
        response = {
            'email': user_data[0]['email'],
            'role': user_data[0]['role'],
        }
        return JsonResponse(response)
    except jwt.ExpiredSignatureError:
        response = {
            'error': 'token is expired!',
        }
        return JsonResponse(response)
    except jwt.exceptions.DecodeError:
        response = {
            'error': 'token is invalid!'
        }
        return JsonResponse(response)
