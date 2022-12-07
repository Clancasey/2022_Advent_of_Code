input_file = open("day1_input.txt","r")
current_line = input_file.readline()
current_calories = 0
elf_calories = []
while current_line:
    if current_line == "\n":
        elf_calories.append(current_calories)
        current_calories = 0
    else:
        current_calories += int(current_line)
    current_line = input_file.readline()

elf_calories.sort(reverse = True)
print("Max calories: " + str(elf_calories[0]))
print("Summation of top 3 elf calories: " + str(elf_calories[0]+elf_calories[1]+elf_calories[2]))
