from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home.models import Restraunt

import json


@csrf_exempt
def StudentAPiView (request ,id=None):
    output = {"data":None,"message":""}

    method = request.method
    if method =="GET":
        if id is None:
         print("========================= GET ================")
        #  p = list(Profile.objects.filter().values("id","first_name"))
         p = list(Restraunt.objects.filter().values('restruant_name','Address','menu_item'))
         output['data'] = p

         
    elif method == "POST":
        data = json.loads(request.body)
        print("json converted data from react",data)
        
        

   
 
    return JsonResponse(output)