import akshare as ak
import django
import pymysql

from AkshareApp.model.models import StockInfoACodeName


def stock_info_a_code_name() -> True or False:
    """
    目标地址: 沪深交易所
    描述: 获取沪深 A 股股票代码和简称数据
    限量: 单次获取所有 A 股股票代码和简称数据
    :return:None
    """
    result = ak.stock_info_a_code_name()
    entries = []
    for e in result.T.to_dict().values():
        entries.append(StockInfoACodeName(**e))
    try:
        StockInfoACodeName.objects.bulk_create(entries)
    except pymysql.err.IntegrityError:
        print("pymysql, 信息重复")
        return False
    except django.db.utils.IntegrityError:
        print("django, 信息重复")
        return False
    return True
