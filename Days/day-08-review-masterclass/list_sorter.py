"""Input 5 numbers, return stats: sorted list, max, min, average."""

user_input = input("Enter 5 numbers (comma-separated): ")

try:
    numbers = [float(num.strip()) for num in user_input.split(",")]

    if len(numbers) != 5:
        print("Please enter exactly 5 numbers.")
    else:
        
        sorted_list = sorted(numbers)
        maximum = max(numbers)
        minimum = min(numbers)
        average = round(sum(numbers) / len(numbers), 2)

        
        print(f"Sorted List: {sorted_list}")
        print(f"Max: {maximum}")
        print(f"Min: {minimum}")
        print(f"Average: {average}")

except ValueError:
    print("Invalid input. Please enter only numbers.")
    
    
