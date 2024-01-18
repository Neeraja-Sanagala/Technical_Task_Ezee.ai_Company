def transform_string(n):
    length = len(n)
    
    if length % 2 != 0:
        mid_point = length // 2
        first_half = n[:mid_point].upper()
        second_half = n[mid_point:].lower()
        transformed_string = first_half + second_half
    else:
        transformed_string = n.lower()

    return transformed_string

str1 = input("Enter a string: ")
result = transform_string(str1)
print(f"Actual string: {str1} \n Transformed string: {result}")