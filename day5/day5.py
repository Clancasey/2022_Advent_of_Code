from collections import deque


input = open("input.txt","r")
full_input = input.readlines()
stacks = [deque() for _ in range(10)]

for i in range(7,-1,-1):
    for j in range(1,10,1):
        current_letter = full_input[i][4*j-3]
        if ord(current_letter) in range(65,91):
            stacks[j].append(current_letter)
print(stacks)

for i in range(10,len(full_input)):
    current_line=full_input[i].strip()
    split_line = current_line.split(' ')
    
    crate_number = int(split_line[1])
    source_stack = int(split_line[3])
    destination_stack = int(split_line[5])
    for j in range(crate_number):
        stacks[destination_stack].append(stacks[source_stack].pop())

top_string = ''
for i in range(1,10,1):
    top_string+=stacks[i].pop()

print(top_string)
