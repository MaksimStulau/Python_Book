"""Создать генератор который будет принимать список и возвращать его уникальные значения"""


def gen_list(input_list):
    seen = set()
    for item in input_list:
        if item not in seen:
            seen.add(item)
            yield item


for num in gen_list([1, 2, 2, 3, 4, 4, 5, 3]):
    print(num)
