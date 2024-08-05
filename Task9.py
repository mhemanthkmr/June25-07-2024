# 
def print_pattern(n):
    for i in range(1,n+1):
        for k in range(1,i+1):
            print(k,end='')
        print()
print_pattern(6)
print_pattern(4)
