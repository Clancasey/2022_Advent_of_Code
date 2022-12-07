input = open("input.txt","r")

for current_line in input:
    current_line = current_line.strip()
    print(current_line)

# must implement 9 stacks, one for each 'stack' of crates
# pop x number off current stack and push those values onto new stack