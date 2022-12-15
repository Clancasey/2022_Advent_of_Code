def is_visible(input, row, col):
    if row == 0 or row == len(input)-1 or col == 0 or col==len(input[0])-1: # returns visible for edge trees
        return True
    tree_height = input[row][col]
    still_visible = True

    for r in range(len(input)):
        if r == row:
            if still_visible: 
                return True
            else:
                still_visible = True
        elif input[r][col] >= tree_height: 
            still_visible=False
    
    if still_visible: 
        return True
    else:
        still_visible = True

    for c in range(len(input[0])):
        if c == col:
            if still_visible:
                return True
            else:
                still_visible=True
        elif input[row][c] >= tree_height: 
            still_visible=False
    

    return still_visible

input = open("day8/input.txt","r")
input = input.readlines()
input = [line.strip() for line in input]

total_visible = 0

for row in range(len(input)):
    for col in range(len(input[0])):
        total_visible += 1 if is_visible(input,row,col) else 0

print('Total visible trees: ' + str(total_visible))