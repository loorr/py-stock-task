from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    db_create_time = models.DateTimeField(auto_now_add=True)
    db_modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
