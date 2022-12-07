import math
input = open("input.txt","r")
priority_list = list(range(97,123)) + list(range(65,91))
print(priority_list)
current_line = input.readline()
score = 0
while current_line:
    compartment1_item_list = []

    if current_line[-1] == '\n': # Removes newline character if it exists at the end of the line
        current_line = current_line[0:len(current_line)-1]
    
    compartment1 = current_line[0:math.floor(len(current_line)/2)]
    compartment2 = current_line[math.floor(len(current_line)/2):len(current_line)]
    
    current_line = input.readline()
    for item in compartment1:
        if not item in compartment1_item_list:
            compartment1_item_list.append(item)
    # print(compartment1_item_list)
    for item in compartment2:
        if item in compartment1_item_list:
            print('Item in both compartments! Item is: ' + item)
            print('This is a priority score of: ' + str(priority_list.index(ord(item))+1))
            score += priority_list.index(ord(item))+1
            break

print('Final priority score: ' + str(score))

# switch case in current line depending on if first, second, or third elf's rucksack
# first elf: create same item_list as in part 1
# second elf: create a new list depending on all items that are common across first & second elf
# third elf: find item that is common between the new list and the thirf elf's rucksack
# calculate priority the same way.
