def pig_latin(word):
    first_letter = word[0]
    rest_of_word = word[1:]
    return rest_of_word + first_letter + "ay"


words = ["hello", "world", "python"]
for i in words:
    print(pig_latin(i))
