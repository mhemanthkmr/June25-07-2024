#task 10 amstrong number

number=int(input("Enter the number:"))
num_str = str(number)
num_length = len(num_str)
sum_of_powers = 0

for i  in num_str:
    sum_of_powers += int(i) ** num_length

if sum_of_powers == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")