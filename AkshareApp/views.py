# Create your views here.
from django.http import HttpResponse

from AkshareApp.model.models import StockList

"""
 django.http模块中定义了HttpResponse 对象的API
 作用：不需要调用模板直接返回数据
 HttpResponse属性：
    content: 返回内容,字符串类型
    charset: 响应的编码字符集
    status_code: HTTP响应的状态码
"""

"""
hello 为一个视图函数，每个视图函数必须第一个参数为request。哪怕用不到request。
request是django.http.HttpRequest的一个实例
"""


def akshare_hello(request):
    sotck = StockList(stock_id="SZ00002", market_symbol="SZ", symbol="00002", name="测试")
    sotck.save()
    return HttpResponse('Hello World')
