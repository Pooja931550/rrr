from django.db import models


class user(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, default=None)
    password = models.CharField(max_length=255, default=None)
    mobile_number = models.CharField(max_length=255, default=None)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    client_key = models.TextField(default=None)

    class Meta:
        db_table = "user"