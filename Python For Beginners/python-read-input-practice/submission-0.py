def add_two_numbers() -> int:
    numbers = input()

    numbers_split = numbers.split(",")

    nums = []

    for num in numbers_split:
        nums.append(int(num))
    
    return sum(nums)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
