from django.http import JsonResponse
from CommonInfra import StateCode


def ok(data, message=StateCode.SUCCESS.message, code=StateCode.SUCCESS.code):
    body = {"data": data, "message": message, "code": code}
    return JsonResponse(body, safe=False)


def fail(data, message=StateCode.BUSSINESS_ERROR.message, code=StateCode.BUSSINESS_ERROR.code):
    body = {"data": data, "message": message, "code": code}
    return JsonResponse(body, safe=False)
