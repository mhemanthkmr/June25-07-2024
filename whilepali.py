word = input("Enter the word:")
reversed_word = ""
index = len(word) - 1

while index >= 0:
    reversed_word += word[index]
    index -= 1

if word == reversed_word:
    print("It is a palindrome")
else:
    print("It is not a palindrome")








