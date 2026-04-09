def calculate_list_values():
    numbers = [1, 2, 3, 4, 5, 6]

    total_sum = 0
    for num in numbers:
        total_sum = total_sum + num

    total_product = 1
    for num in numbers:
        total_product = total_product * num

    print("Sum:", total_sum)
    print("Product:", total_product)


calculate_list_values()