input = open("input.txt","r").readline()

marker_list = []
for i in range(len(input)):
    for marker in marker_list:
        if ord(input[i]) == marker:
            marker_list = []
            break

    marker_list.append(ord(input[i]))
    if len(marker_list) == 13:
        solution = i+1
        break

print("Part 1 solution: " + str(solution) + ", with marker: " + input[solution-14:solution])