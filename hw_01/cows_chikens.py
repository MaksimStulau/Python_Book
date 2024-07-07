"""https://www.codewars.com/kata/574c5075d27783851800169e"""

num_h = 72
num_l = 200
chikens = 0
cows = 0


if num_h == 0 and num_l == 0:
    result = (0, 0)

if num_l % 2 != 0:
    result = "No solutions"

else:

    chikens = 2 * num_h - num_l // 2
    cows = num_l // 2 - num_h

    if chikens < 0 or cows < 0:
        result = "No solutions"

    else:
        result = (chikens, cows)

print(f'{chikens}, {cows} => {result}')
