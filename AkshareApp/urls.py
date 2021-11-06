
from django.conf.urls import url
from django.urls import path

from AkshareApp.controller.views import akshare_index, get_stock_item, stock_info_a_code_name

urlpatterns = [
    path("", akshare_index),
    url("get-stock-item", get_stock_item),
    url("stock-info-a-code-name", stock_info_a_code_name)
]