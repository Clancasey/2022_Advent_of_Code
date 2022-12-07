input = open("input.txt","r")
combinations = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}
new_combinations = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7 
}
current_score = 0 
new_score = 0
current_line = input.readline()
while current_line:
    if current_line[-1] == '\n': # Removes newline at end of each line. This could be improved by using readline(3) to only read the first 3 characters of each line.
        current_line = current_line[0:len(current_line)-1]
    current_score += combinations[current_line]
    new_score += new_combinations[current_line]
    current_line = input.readline()

print("Initial score: " + str(current_score))
print("New score: " + str(new_score))
