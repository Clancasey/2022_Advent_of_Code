class Folder:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
    size = 0

input = open("day7/input.txt","r")





for line in input:

    line = line.strip()
    # print(line)

    if line == '$ cd /':
        folder_list = [Folder('/')]
        current_folder = folder_list[0]
        continue

    if line[0] == '$': # Detected a command
        if line[2:4] == 'cd':
            if line [5:7] == '..':
                current_folder.parent.size += current_folder.size
                current_folder = current_folder.parent
                # print("current folder: " + current_folder.name + " parent folder: " + str(current_folder.parent))
            else:
                current_folder = next(child_folder for child_folder in current_folder.children if child_folder.name == line[5:len(line)])
                # print("current folder: " + current_folder.name + " parent folder: " + str(current_folder.parent))

    if 48 <= ord(line[0]) <= 57: # Detected a file
        current_folder.size += int(line.split(' ')[0])

    if line[0:3] == 'dir': # Detected a directory
        folder_list.append(Folder(line[4:len(line)]))
        current_folder.children.append(folder_list[len(folder_list)-1])
        folder_list[len(folder_list)-1].parent = current_folder
        # print('dir ' + line[4:len(line)] + ' added with parent dir of ' + current_folder.name)

small_folders_size = 0

for folder in folder_list:
    if folder.size <= 100000:
        small_folders_size += folder.size
        # print(folder.name + ", size of " + str(folder.size))

print('Total folder size for all folders <= 100,000: ' + str(small_folders_size))