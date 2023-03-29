from ..serializers.CheckwhitelistedSerializer import CheckURLWhitelist
from ..databaseModels.Checkwhitelisted import CheckURLWhitelist

def CheckURLWhitelistService(questionId):
    inputField = CheckURLWhitelist.objects.filter(ip_address='ip_address')
    print('****',inputField)
    serializer = CheckURLWhitelist(inputField, many=True)

    return (serializer.data)