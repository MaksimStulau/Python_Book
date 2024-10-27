"""Создать генератор который будет распаковывать по одному значению из списка списков"""


def unpack_nested_lists(nested_list):
    for sublist in nested_list:
        for item in sublist:
            yield item


for value in unpack_nested_lists([[1, 2], [3, 4], [5, 6]]):
    print(value)

