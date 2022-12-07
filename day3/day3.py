import math
input = open("input.txt","r")
priority_list = list(range(97,123)) + list(range(65,91))
print(priority_list)
current_line = input.readline()
score = 0
part2_score = 0
elf_counter = 0
common_item_list = []
double_common_item_list = []
while current_line:
    compartment1_item_list = []

    if current_line[-1] == '\n': # Removes newline character if it exists at the end of the line
        current_line = current_line[0:len(current_line)-1]
    
    compartment1 = current_line[0:math.floor(len(current_line)/2)]
    compartment2 = current_line[math.floor(len(current_line)/2):len(current_line)]
    
    for item in compartment1:
        if not item in compartment1_item_list:
            compartment1_item_list.append(item)
    for item in compartment2:
        if item in compartment1_item_list:
            print('Item in both compartments! Item is: ' + item)
            print('This is a priority score of: ' + str(priority_list.index(ord(item))+1))
            score += priority_list.index(ord(item))+1
            break
        
    if elf_counter == 0:
        for item in current_line:
            if not item in common_item_list:
                common_item_list.append(item)
    elif elf_counter == 1:
        for item in current_line:
            if item in common_item_list and not item in double_common_item_list:
                double_common_item_list.append(item)
    elif elf_counter == 2:
        for item in current_line:
            if item in double_common_item_list:
                print('Security tag discovered! Item is: ' + item)
                print('This is a priority score of: ' + str(priority_list.index(ord(item))+1))
                part2_score += priority_list.index(ord(item))+1
                break

    if elf_counter < 2:
        elf_counter+= 1
    else:
        elf_counter = 0
        common_item_list = []
        double_common_item_list = []

    current_line = input.readline()

print('Final priority score part 1: ' + str(score))
print('Final priority score part 2: ' + str(part2_score))

# switch case2 in current line depending on if first, second, or third elf's rucksack
# first elf: create same item_list as in part 1
# second elf: create a new list depending on all items that are common across first & second elf
# third elf: find item that is common between the new list and the thirf elf's rucksack
# calculate priority the same way.
