def sudoku(file):
    fich = open(file,'r')
    mots = list(fich.read())

    try:
        while True:
            mots.remove('|')
    except ValueError:
        pass
    try:
        while True:
            mots.remove('\n')
    except ValueError:
        pass
    try:
        while True:
            mots.remove('+')
    except ValueError:
        pass
    try:
        while True:
            mots.remove('-')
    except ValueError:
        pass
    mots = list(zip(*[iter(mots)] * 9))
    mots_list=[[0 for x in range(9)] for y in range(9)]
    for i in range(9):
        
        mots_list[i]=list(mots[i])
    solve(mots_list)
    return print_board(mots_list)
    
def solve(bo):

    
    find = find_empty(bo)
    
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            

            if solve(bo):
                return True

        bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        
        if bo[pos[0]][i]==str(num) and pos[1]!=i:
            
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("---+---+--- ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) , end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == "_":
                return (i, j)  # row, col
                

    return None




    


sudoku("s.txt")


