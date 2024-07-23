word = input("Enter the word:")
reversedWord = ""

for char in word:
    reversed_word = char + reversedWord

if word == reversedWord:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
