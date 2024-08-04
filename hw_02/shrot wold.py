#Определить длину самого короткого слова в заданной строке

def short_wold():

    string = input("Enter a string: ")

    wold = string.split()
    return min(wold, key=len)


print(short_wold())
