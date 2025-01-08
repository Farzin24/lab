numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
positive_numbers = []
for num in numbers:
    if num > 0:
        positive_numbers.append(num)
print(positive_numbers)

