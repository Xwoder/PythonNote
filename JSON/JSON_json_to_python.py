import json

"""
json.loads: JSON 数据 -> Python 数据
"""

data_json: str = """
                [
                    {
                        "a": 1,
                        "b": 2,
                        "c": 3,
                        "d": 4,
                        "e": 5
                    }, {
                        "a": 6,
                        "b": 7,
                        "c": 8,
                        "d": 9,
                        "e": 10
                    }
                ]
"""

data_py: list[dict[str, int]] = json.loads(data_json)

print(
    # <class 'list'>
    type(data_py)
)

print(
    # [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, {'a': 6, 'b': 7, 'c': 8, 'd': 9, 'e': 10}]
    data_py
)
