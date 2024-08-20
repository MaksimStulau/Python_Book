# Проверить уникальность элементов в списке с произвольной вложенностью списков.

def are_elements_unique(lst):

    seen = set()
    for i in lst:
        if isinstance(i, list):
            if not are_elements_unique(i):
                return False
        else:
            if i in seen:
                return False
            seen.add(i)
    return True


list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, [3, 4], 5]
list3 = [1, 2, [3, 4, 3], 5]

print(are_elements_unique(list1))
print(are_elements_unique(list2))
print(are_elements_unique(list3))
