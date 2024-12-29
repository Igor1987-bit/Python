my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    if my_list[i] == 0:
        i = i + 1           # т.к. возврат к началу, i + 1
        continue            # возврат к началу
    elif my_list[i] < 0:    # завершение цикла
        break
    print(my_list[i])
    i = i + 1
# consol
# 42
# 69
# 322
# 13
# 99
