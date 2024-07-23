word=input("Enter the word:")
returnword=" "
for i in word:
    returnword=i+returnword
if (word==word[::-1]):
    print("It is palindrome")
else:
    print("It is not a palindrome")