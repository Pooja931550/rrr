from django.db import models

# Create your models here.



from .databaseModels.clientMaster import ClientMaster
# from .databaseModels.Checkwhitelisted import CheckURLWhitelist
from .databaseModels.url_whitelist import URLWhitelist
from .databaseModels.user import user