string = input("enter palidrome in question: ")
rev_string = string[::-1]
print("reversed string:", rev_string)
if string == rev_string:
    print("string is a palindrome")
else:
    ("string is not a palidrome")
