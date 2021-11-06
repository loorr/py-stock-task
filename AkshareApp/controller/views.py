from AkshareApp.service import CommonDataService
from CommonInfra.BaseResponse import ok


def akshare_index(request):
    return ok("hello akshare")


def get_stock_item(request):
    return ok(True)


def stock_info_a_code_name(request):
    CommonDataService.stock_info_a_code_name()
    return ok(True)
