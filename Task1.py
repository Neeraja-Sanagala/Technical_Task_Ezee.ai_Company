import re
def new_string(n):
    new_string = re.sub(r'\d', '', n)
    new_string = re.sub(r'[^a-zA-Z0-9\s]', ' ', new_string)
    
    return new_string


str1 = input("Enter a string: ")

result = new_string(str1)

print("Original String:", str1)
print("New String:", result)