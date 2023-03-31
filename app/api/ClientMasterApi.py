
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..databaseModels.clientMaster import ClientMaster
import requests
from ..serializers.CheckwhitelistedSerializer import ClientMasterSerializer
from ..databaseService.ClientMasterService import Client


class UserAuthAPI(APIView):
    def post(self, req):
        client_key = req.data.get('clientkey')
        url = req.headers.get('url')
        auth_response = Client(client_key,url)
        if auth_response:
            return Response(auth_response, status.HTTP_200_OK)
        else:
            return Response("Data not found")
            




  
    