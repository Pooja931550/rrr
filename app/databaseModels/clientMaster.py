from django.db import models
import uuid
from ..databaseModels.user import user


class   ClientMaster(models.Model):
    clientID = models.AutoField(primary_key=True)
    clientName = models.CharField(max_length=50, null=True)
    clientCode = models.CharField(max_length=255, null=True)
    clientType = models.CharField(max_length=255, null=True)
    clientURL = models.TextField(null=True)
    clientkey = models.TextField(max_length=255, default=uuid.uuid4())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    url_whitelisting = models.BooleanField(default=True)
    # user = models.ForeignKey(user, null=False, blank=False, on_delete=models.CASCADE, db_column='user',
    #                          related_name="user")

    class Meta:
        db_table = 'ClientMaster'
