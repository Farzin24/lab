user_input = input("Enter a list of integers separated by spaces: ")
result = []

for num in user_input.split():
    if int(num) > 100:
        result.append("over")
    else:
        result.append(int(num))

print("Modified list:", result)
