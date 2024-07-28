""" Task 1
Formatted String
Create a list of dictionaries where each dictionary represents a student with name and score keys.
 Use a formatted string to print each student's name and score in a sentence. For example: "John scored 85 marks."""

# List of dictionaries representing students
students = [
    {"name": "John", "score": 85},
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 78},
    {"name": "Emma", "score": 88},
    {"name": "Michael", "score": 90}
]

# Print each student's name and score using formatted strings
for student in students:
    print(f"{student['name']} scored {student['score']} marks.")





"""Slicing and Indexing
Create a list containing the numbers from 1 to 10. Print the following slices:

The first three elements.
The last three elements.
Every second element from the list."""

# Create the list of numbers from 1 to 10
numbers = list(range(1, 11))

# Print the first three elements
print("The first three elements:", numbers[:3])

# Print the last three elements
print("The last three elements:", numbers[-3:])

# Print every second element from the list
print("Every second element:", numbers[1::2])
