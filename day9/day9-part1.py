input = open("day9/input.txt","r")

for line in input:
    line = line.strip()
    print(line)
# The storage of all locations the tail have been could be solved used a list, where 'row,col' is added to the list if it doesn't yet exist in the list.
#  len(list) is returned as final solution
