def check_north(input,row,col,tree_height):
    score = 0
    if row == 0: 
        return score
    score = 1 
    if input[row-1][col] < tree_height:
        score += check_north(input,row-1,col,tree_height)
    return score

def check_south(input,row,col,tree_height):
    score = 0
    if row == len(input)-1: 
        return score
    score = 1 
    if input[row+1][col] < tree_height:
        score += check_south(input,row+1,col,tree_height)
    return score

def check_east(input,row,col,tree_height):
    score = 0
    if col == len(input[0])-1: 
        return score
    score = 1 
    if input[row][col+1] < tree_height:
        score += check_east(input,row,col+1,tree_height)
    return score

def check_west(input,row,col,tree_height):
    score = 0
    if col == 0: 
        return score
    score = 1 
    if input[row][col-1] < tree_height:
        score += check_west(input,row,col-1,tree_height)
    return score

input = open("day8/input.txt","r")
input = input.readlines()
input = [line.strip() for line in input]


highest_scenic_score = 0

for row in range(len(input)):
    for col in range(len(input[0])):
        scenic_score = check_north(input,row,col,input[row][col])
        scenic_score *= check_south(input,row,col,input[row][col])
        scenic_score *= check_east(input,row,col,input[row][col])
        scenic_score *= check_west(input,row,col,input[row][col])
        if scenic_score > highest_scenic_score: highest_scenic_score = scenic_score


print('Highest scenic score: ' + str(highest_scenic_score))