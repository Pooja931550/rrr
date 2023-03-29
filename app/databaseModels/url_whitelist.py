from django.db import models


class URLWhitelist(models.Model):
    id = models.AutoField(primary_key=True)
    url_address = models.CharField(max_length=250, null=False, blank=False, unique=True)
    ip_address = models.CharField(max_length=250, null=False, blank=False, unique=True)
    user = models.ForeignKey("ClientMaster", null=False, blank=False, on_delete=models.CASCADE, db_column="user",
                             related_name="client_user")
    status = models.BooleanField(default=False, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(null=False, blank=False)
    created_by = models.ForeignKey("ClientMaster", null=False, blank=False, on_delete=models.CASCADE,
                                   db_column='created_by', related_name="created_by")
    updated_by = models.ForeignKey("ClientMaster", null=False, blank=False, on_delete=models.CASCADE,
                                   db_column='updated_by', related_name="updated_by")
    is_active = models.BooleanField()

    class Meta:
        db_table = "url_whitelist"