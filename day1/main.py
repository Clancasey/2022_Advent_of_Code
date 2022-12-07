input_file = open('day1_input.txt')
current_line = input_file.readline
max_calories = 0
current_calories = 0
while current_line:
    if current_line == "\n":
        if current_calories > max_calories:
            max_calories = current_calories
        current_calories = 0
    else:
        current_calories += int(current_line)
    current_line = input_file.readline

print(max_calories)