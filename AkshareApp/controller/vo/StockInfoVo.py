from rest_framework import serializers

class BaseVo(serializers.Serializer):
    pass

class SotckInfoVo(BaseVo):
    stock_id = serializers.CharField(max_length=10)
    market_symbol = serializers.CharField(max_length=10)
    symbol = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=10)
    full_name = serializers.CharField(max_length=10)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
