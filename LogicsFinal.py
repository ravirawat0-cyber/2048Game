import random

#! making 4X4 matirx with 0 element
def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

#! adding 2 into the matrix into the random postion with random row and column generator
def add_new_2(mat):

    # random number genrating
    r = random.randint(0,3)
    c = random.randint(0,3)

    # generate till row/col with ele 0 found
    while(mat[r][c] != 0):
        r = random.randint(0,3)
        c = random.randint(0,3)
    # adding 2 
    mat[r][c] = 2

#! shift all non element to left 
def compress(mat):
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)

    # shifting all non element to left
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
 
    return new_mat, changed


#! now multiplying the consecutive element
def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
                changed = True

    return mat, changed

    
#! reverse a matirx
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])

    return new_mat 

#! transpose of matrix
def transpose(mat):

    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    
    return new_mat


#! Left move 
def move_left(grid):
    new_grid, changed1 = compress(grid)
    new_grid, changed2 = merge(new_grid)
    #checking if any change or not
    changed = changed2 or changed1
    new_grid, temp = compress(new_grid)
    return new_grid, changed


#! right move 
def move_right(grid):
    reversed_grid = reverse(grid)
    new_grid, changed1 = compress(reversed_grid)
    new_grid, changed2 = merge(new_grid)
    # Checking if any change or not
    changed = changed2 or changed1
    new_grid = compress(new_grid)
    new_grid = reverse(new_grid)

    return new_grid, changed



#! up move 
def move_up(grid):
    transpose_grid = transpose(grid)
    new_grid, changed1 = compress(transpose_grid)
    new_grid, changed2 = merge(new_grid)
    # Checking if any change or not
    changed = changed1 or changed2
    new_grid = compress(new_grid)
    new_grid = transpose(new_grid)
    return new_grid, changed

#! down move 
def move_down(grid):
    transpose_grid = transpose(grid)
    reverse_grid = reverse(grid)
    new_grid,changed1 = compress(reverse_grid)
    new_grid,changed2 = merge(new_grid)
    # checking if any change or not
    changed = changed1 or changed2
    new_grid = compress(new_grid)
    reverse_grid = compress(new_grid)
    transpose_grid = transpose(reverse_grid)
    return transpose_grid, changed
    

#! cheacking for the game state 
def get_current_state(mat):
    # check for 2048 value 
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 2048):
                return "WON"
    
    # check if any 0 present
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 0):
                return 'GAME NOT OVER'

    
    # Every row and column except last one
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return 'GAME NOT OVER'

    
    # Checking for last row 
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return 'GAME NOT OVER'

    # checking for last column
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return "GAME NOT OVER"

    
    # if all the condition is fail then
    return 'LOST'