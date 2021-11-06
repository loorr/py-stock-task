from django.http import HttpResponse, JsonResponse

from AkshareApp.model.models import StockList
import AkshareApp.controller.vo.StockInfoVo as StockInfoVo
from CommonInfra.BaseResponse import ok


def akshare_hello(request):
    sotck = StockList(stock_id="SZ00002", market_symbol="SZ", symbol="00002", name="测试")
    sotck.save()
    return HttpResponse('Hello World')


def get_stock_item(request):
    # sotck = StockList.objects.all()
    # result = StockInfoVo.SotckInfoVo(instance=sotck, many=True)
    data = True
    return ok(data)
