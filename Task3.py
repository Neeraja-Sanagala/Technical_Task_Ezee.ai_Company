
def second_and_fourth_greatest(numbers):
    if len(numbers) < 4:
        return "List should have at least 4 numbers."

    sorted_numbers = sorted(numbers, reverse=True)
    second_greatest = sorted_numbers[1]
    fourth_greatest = sorted_numbers[3]

    return second_greatest, fourth_greatest


try:
    
    num_list = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]

    
    result = second_and_fourth_greatest(num_list)

    
    print(f"Second greatest number: {result[0]}")
    print(f"Fourth greatest number: {result[1]}")

except ValueError:
    print("Error: Please enter valid numbers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")