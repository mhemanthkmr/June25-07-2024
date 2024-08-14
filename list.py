my_list = [10, 12, 14, 10, 16, 14, 18]
for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] == my_list[j]:
            print(my_list[i])
            break
