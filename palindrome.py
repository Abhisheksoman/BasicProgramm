s=str(input("Enter a string"))
print(s)
if s==s[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
