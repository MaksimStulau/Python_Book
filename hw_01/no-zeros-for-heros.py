def no_zeros_for_heros(num):

    str_num = str(num)
    str_num = str_num.rstrip('0')
    return int(str_num) if str_num else 0


print(no_zeros_for_heros(1010))
