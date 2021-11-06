class ReponseInfo:
    def __init__(self, message, code):
        self.message = message
        self.code = code


SUCCESS = ReponseInfo("success", "10000")
BUSSINESS_ERROR = ReponseInfo("system bussiness", "20000")
PARAMETER_ERROR = ReponseInfo("参数错误", "20001")

