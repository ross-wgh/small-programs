board = [
    [2,4,0,5,7,3,8,9,0],
    [1,3,8,9,2,6,5,7,4],
    [9,0,5,8,4,1,2,6,3],
    [3,9,0,7,1,5,6,2,8],
    [5,8,1,6,3,2,9,4,0],
    [0,2,7,0,9,8,3,1,5],
    [0,0,2,0,8,0,4,0,6],
    [0,0,3,2,6,7,1,8,9],
    [0,6,0,1,0,0,0,3,2]
]

iterations = 0



def print_board(sudoku_board): #print board
    for i in range(len(sudoku_board)):
        for j in range(len(sudoku_board[0])):
            if j == 2 or j == 5:
                print(board[i][j], end=" | ")
            elif j == 8 and (i ==2 or i ==5):
                print(board[i][j], end="\n")
                print("-"*35)
            else:
                print(board[i][j], end="   ")
        if i != 2 and i!=5:
            print("\n")    

def find_empty(sudoku_board):
    for i in range(len(sudoku_board)):
        for j in range(len(sudoku_board[0])):
            if sudoku_board[i][j] == 0:
                return (i,j) #return position of empty space
    return
            
def is_valid(sudoku_board, num, position):
    #1. Check Row #2. Check column. #3. Check local square
    for i in range(len(sudoku_board[0])): #row
        if sudoku_board[position[0]][i] == num and position[1] !=i:
            return False
    for i in range(len(sudoku_board)): #column
        if sudoku_board[i][position[1]] == num and position[0] !=i:
            return False
    #determine box
    box_x = position[1]//3
    box_y = position[0]//3
    
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if sudoku_board[i][j] == num and (i,j) != position:
                return False    
    return True

def solve(board):
    global iterations
    iterations +=1
    find = find_empty(board)
    if not find: #if there are no empty spaces on the board
        if 0 in board:
            print("Unsolvable")
            return False
        else:
            for i in range(0,9): #nested for checks if the final solution is valid, if not the sudoku is unsolvable
                for j in range(0,9):
                    if not is_valid(board, board[i][j], (i,j)):
                        print("Unsolvable")              
                        return False
             
                            
        print("FINAL BOARD:")
        print_board(board)
        print("It took", iterations, "iterations to perform the solving algorithm")
        return True
    else:
        row,col = find
    
    for i in range(1,10):
        if(is_valid(board, i, (row, col))):
            board[row][col]=i
            if solve(board):
                return True
            
            board[row][col]=0
            
    
    return False   
        
def main():
    print_board(board)
    solve(board)

    


if __name__ == "__main__":
    main()