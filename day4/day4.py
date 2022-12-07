input = open("input.txt","r")
current_line = input.readline()
score = 0
second_score = 0
while current_line:
    if current_line[-1] == '\n': # Removes newline character if it exists at the end of the line
        current_line = current_line[0:len(current_line)-1]
    range_list = current_line.split(',')
    first_range_list = range_list[0].split('-')
    second_range_list = range_list[1].split('-')
    print("from " + str(first_range_list[0]) + " to " + str(first_range_list[1]) + " and "+ str(second_range_list[0]) + " to " + str(second_range_list[1]))
    if (int(first_range_list[0])>=int(second_range_list[0]) and int(first_range_list[1])<=int(second_range_list[1])) or (int(first_range_list[0])<=int(second_range_list[0]) and int(first_range_list[1])>=int(second_range_list[1])):
        score +=1
    if (int(second_range_list[0])<=int(first_range_list[1]) and int(second_range_list[0])>=int(first_range_list[0])) or (int(first_range_list[0])<= int(second_range_list[1]) and int(first_range_list[0])>= int(second_range_list[0])):
        print("overlapped!")
        second_score += 1
    print(str(range_list)+ " score:" + str(score))
    current_line = input.readline()

print("score for first part: " + str(score))
print("score for second part: " + str(second_score))

