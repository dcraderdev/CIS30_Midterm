def transform_data(numbers):
    try:
        squared_numbers = [num ** 2 for num in numbers]

        total_sum = sum(squared_numbers)

        return squared_numbers, total_sum

    except TypeError:
        print("Error: Input must be a list of integers.")    


numbers = [1, 2, 3, 4, 5]
squared_list, squared_sum = transform_data(numbers)
print("Squared List:", squared_list)
print("Sum of Squared Values:", squared_sum)