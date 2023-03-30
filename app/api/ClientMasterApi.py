
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..databaseModels.clientMaster import ClientMaster
# from django.core.exceptions import ObjectDoesNotExist
import requests
from ..serializers.CheckwhitelistedSerializer import ClientMasterSerializer


class ClientMasterApi(APIView):
    def post(self, request):
        client_key = request.data.get('clientkey')
        url = request.headers.get('url')
        try:
            user_obj = ClientMaster.objects.get(clientkey=client_key)
            serializer = ClientMasterSerializer(user_obj).data

            if serializer['clientURL']!=url:
                return Response({"message": "url Invalid "})
            elif serializer['is_active']!=True:
                return Response({"message": "status invalid"})   
            return Response(serializer)
        except ClientMaster.DoesNotExist:
               return Response({"message": "Invalid client key "}, status=status.HTTP_400_BAD_REQUEST)





  
    