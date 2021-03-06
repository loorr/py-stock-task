from django.db import models
from CommonInfra.Utils import BaseModel

# 常量
APP_DB_PREFIX = "akshare_"


class StockList(BaseModel):
    stock_id = models.CharField(max_length=10, unique=True)
    market_symbol = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    full_name = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = APP_DB_PREFIX + 'stock_list'


class StockInfoACodeName(BaseModel):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = APP_DB_PREFIX + 'stock_info_a_code_name'
