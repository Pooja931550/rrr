
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..databaseModels.clientMaster import ClientMaster
from ..serializers.CheckwhitelistedSerializer import ClientMasterSerializer



def Client(client_key,url):
    user_obj = ClientMaster.objects.get(clientkey=client_key)
    serializer = ClientMasterSerializer(user_obj).data
    if serializer['clientURL']!=url:
        return ({
                'status': False,
                'message': 'Your Url is Invalid !!'
        })
    elif serializer['is_active']!=True:
        return ({
                'status': False,
                'message': 'Your Status  is Invalid !!'       
        })   
    return ({"data" : serializer, "status" : True})


    


  
    