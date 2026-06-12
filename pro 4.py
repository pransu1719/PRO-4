
  print("Welcome to the Data Analyzer and Transformer Program")   
  print("1. Input Data")
  print("2. Display Data Summary (Built-in Functions)") 
  print("3. Calculate Factorial (Recursion)")
  print("4. Filter Data by Threshold (Lambda Function)")
  print("5. Sort Data")
  print("6. Display Dataset Statistics (Return Multiple Values)")
  print("7. Exit Program")

  choice = int(input("Please enter your choice: "))


  if choice == 1:
     print("Step 1: Input Data")

     data = list(map(int, input( "Enter data for a 1D array (separated by spaces): ").split()))

     print("Data has been stored successfully!")

  else:
    print("Please select option 1.")

# Step 2: Display Data Summary (Built-in Functions)

data = [34, 12, 56, 78, 43, 21, 90]

print("Step 2: Display Data Summary (Built-in Functions)")
print("\nData Summary:")
print("- Total elements:", len(data))
print("- Minimum value:", min(data))
print("- Maximum value:", max(data))
print("- Sum of all values:", sum(data))
print("- Average value:", round(sum(data) / len(data), 2))

# Step 3: Calculate Factorial (Recursion)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Step 3: Calculate Factorial (Recursion)")

num = int(input("Enter a number to calculate its factorial: "))

print(f"Factorial of {num} is: {factorial(num)}")

# Step 4: Filter Data by Threshold (Lambda Function)

data = [12, 21, 34, 43, 56, 78, 90]

print("Step 4: Filter Data by Threshold (Lambda Function)")

if choice == 4:
    print("\nEnter a threshold value to filter out data above this value:")
    threshold = int(input())

    filtered_data = list(filter(lambda x: x >= threshold, data))

    print(f"\nFiltered Data (values >= {threshold}):")
    print(*filtered_data, sep=", ")
else:
    print("Invalid choice!")

# Step 5: Sort Data

data = [56, 12, 90, 34, 21, 78, 43]
print("Choose sorting option:")
print("1. Ascending")
print("2. Descending")


if choice == 1:
    sorted_data = sorted(data)
    print("\nSorted Data in Ascending Order:")
    print(*sorted_data, sep=", ")

elif choice == 2:
    sorted_data = sorted(data, reverse=True)
    print("\nSorted Data in Descending Order:")
    print(*sorted_data, sep=", ")

else:
    print("Invalid choice!")

# Step 6: Display Dataset Statistics (Return Multiple Values)

data = [12, 21, 34, 43, 56, 78, 90]

def dataset_statistics(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    return minimum, maximum, total, average


if choice == 6:
    min_val, max_val, total_val, avg_val = dataset_statistics(data)

    print("\nDataset Statistics:")
    print(f"- Minimum value: {min_val}")
    print(f"- Maximum value: {max_val}")
    print(f"- Sum of all values: {total_val}")
    print(f"- Average value: {avg_val:.2f}")
else:
    print("Invalid choice!")

# Step 7: Exit Program


print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
