"""Создать с помощью класса итератор который будет принимать значения start, stop (целые числа)
и возвращать по очереди значения от старта до стопа"""


class RangeIterator:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


iter_ = RangeIterator(1, 5)
for num in iter_:
    print(num)
