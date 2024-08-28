## Loops and Conditions in Python

This document provides an overview of loops and conditional statements in Python, including examples and explanations.

### 1. Conditional Statements

Conditional statements allow you to execute different blocks of code based on whether a certain condition is True or False. 

#### 1.1.  `if` statement:

The `if` statement is the most basic conditional statement. It executes a block of code only if the condition following it evaluates to True.

```python
# Example
temperature = 25

if temperature > 30:
  print("It's a hot day!")
```

#### 1.2. `else` statement:

The `else` statement is used in conjunction with `if`. It executes a block of code if the condition in the preceding `if` statement is False.

```python
# Example
temperature = 25

if temperature > 30:
  print("It's a hot day!")
else:
  print("It's not so hot today.")
```

#### 1.3. `elif` statement:

The `elif` statement (short for "else if") allows you to check multiple conditions sequentially. If the condition in the `if` statement is False, it checks the condition of the next `elif` statement, and so on.

```python
# Example
temperature = 25

if temperature > 30:
  print("It's a hot day!")
elif temperature > 20:
  print("It's a pleasant day.")
else:
  print("It's a bit chilly.")
```

#### 1.4. Nested Conditions:

You can nest conditional statements inside each other for more complex logic.

```python
# Example
temperature = 25
is_raining = True

if temperature > 20:
  if is_raining:
    print("It's warm but rainy.")
  else:
    print("It's a perfect day for a picnic!")
else:
  print("It's too cold to go out.")
```

### 2. Loops

Loops allow you to execute a block of code repeatedly as long as a certain condition is met.

#### 2.1.  `for` loop:

The `for` loop iterates over a sequence (like a list, tuple, string, or range) and executes the code block once for each item in the sequence.

```python
# Example 1: Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

# Example 2: Using range() function
for i in range(1, 6):  # Prints numbers from 1 to 5
  print(i)
```

#### 2.2. `while` loop:

The `while` loop executes a block of code repeatedly as long as the condition following it remains True.

```python
# Example
count = 0
while count < 5:
  print("Count:", count)
  count += 1  # Important: Update the counter variable
```

#### 2.3. Loop Control Statements:

- `break`: Exits the loop prematurely, even if the loop condition is True.
- `continue`: Skips the current iteration of the loop and continues with the next iteration.

```python
# Example using break and continue
for i in range(1, 11):
  if i == 3:
    continue  # Skip printing 3
  if i == 8:
    break  # Exit loop when i is 8
  print(i)
```

#### 2.4. Nested Loops:

You can nest loops inside each other for more complex iterations.

```python
# Example: Printing a pattern
for i in range(1, 6):
  for j in range(i):
    print("*", end="")
  print()  # Move to the next line
```

### 3. Combining Loops and Conditions:

You can combine loops and conditional statements to create powerful and flexible code.

```python
# Example: Finding even numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for number in numbers:
  if number % 2 == 0:  # Check if the number is even
    even_numbers.append(number)

print("Even numbers:", even_numbers)
```
