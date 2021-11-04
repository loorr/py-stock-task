from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    db_create_time = models.DateTimeField(auto_now_add=True)
    db_modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StockList(BaseModel):
    stock_id = models.CharField(max_length=10, unique=True)
    market_symbol = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    full_name = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = 'stock_list'
