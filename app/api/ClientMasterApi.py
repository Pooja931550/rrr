
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..databaseModels.clientMaster import ClientMaster
import requests
from ..serializers.CheckwhitelistedSerializer import ClientMasterSerializer

class ClientMasterApi(APIView):
    def post(self, req):
        clientkey = req.data.get('clientkey')
        url = req.headers.get('url')
        try:
            user_obj = ClientMaster.objects.get(clientkey = clientkey, clientURL = url, status=1)
            serializer = ClientMasterSerializer(user_obj).data
            return Response({"message": "Valid","data":serializer}, status=status.HTTP_200_OK)       
        except ClientMaster.DoesNotExist:
            return Response({"message": " Not Valid" }, status=status.HTTP_400_BAD_REQUEST)
    

        
            
        


    