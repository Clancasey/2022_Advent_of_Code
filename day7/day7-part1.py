input = open("day7/input.txt","r")

for line in input:
    line = line.strip()
    print(line)
    if line[0] == '$': # Detected a command
        print('detected a command') 
    if 48 <= ord(line[0]) <= 57: # Detected a file
        print('detected a file')
    if line[0:3] == 'dir': # Detected a directory
        print('detected a directory')