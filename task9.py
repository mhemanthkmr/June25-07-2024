def print_pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')
        print()
print_pattern(3)
print_pattern(4)
