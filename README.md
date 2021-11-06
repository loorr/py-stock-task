# 记录

1. 创建app
```shell
django-admin startapp tushareApp
```


2. 数据迁移

```python
# 生成文件
python3 manage.py makemigrations

# 持久化都数据库
python3 manage.py migrate
```