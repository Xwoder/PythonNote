import json

"""
json.dumps: Python 数据 -> JSON 数据

Python 的 JSON 数据本质上是就是一个字符串
"""

# Python 类型数据
data: list[dict[str, int]] = [
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    {'a': 6, 'b': 7, 'c': 8, 'd': 9, 'e': 10},
]

# JSON 类型数据
data_json: str = json.dumps(data)

print(
    # <class 'str'>
    type(data_json)
)

print(
    # [{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}, {"a": 6, "b": 7, "c": 8, "d": 9, "e": 10}]
    data_json
)
