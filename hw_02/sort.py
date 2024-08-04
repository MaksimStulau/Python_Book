#Отсортировать слова в строке по возрастанию их длины

def sort_wold():
    string = input("Enter a string: ")
    words = string.split()
    words.sort(key=len)
    return words


print(sort_wold())
