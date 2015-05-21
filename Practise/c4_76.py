# 76) Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.  [LeetCode]
#         A region is captured by flipping all 'O's into 'X's in that surrounded region.
#         For example,
#             X X X X
#             X O O X
#             X X O X
#             X O X X
#         After running your function, the board should be:
#             X X X X
#             X X X X
#             X X X X
#             X O X X

def preProcess(board,numberOfRows,numberOfCols):
    #Find the indices of all Os in the borders. This are the routes to escape
    boundaryZero = list()
    boundaryZero += [(0,col) for col in xrange(numberOfCols) if board[0][col] == "O"]
    boundaryZero += [(numberOfRows-1,col) for col in xrange(numberOfCols) if board[numberOfRows-1][col] == "O"]
    boundaryZero += [(row,0) for row in xrange(numberOfRows) if board[row][0] == "O"]
    boundaryZero += [(row,numberOfCols-1) for row in xrange(numberOfRows) if board[row][numberOfCols-1] == "O"]
    discovered = set()
    freePathExists = set()
    #Any element adjacent to a index where freePath exist, is also free. So we perform a bfs from every 
    # "O" element in the border to get a list of all indices where free path exist
    for element in boundaryZero:
        queue = list()
        if element not in discovered:
            queue.append(element)
            discovered.add(element)
        while queue :
            (row,col) = queue.pop(0)
            freePathExists.add((row,col))
            if col - 1 >= 0 and board[row][col-1] == "O" and (row,col-1) not in discovered :
                queue.append((row,col-1))
                discovered.add((row,col-1))
            if col + 1 < numberOfCols and board[row][col+1] == "O" and (row,col+1) not in discovered :
                queue.append((row,col+1))
                discovered.add((row,col+1))
            if row - 1 >= 0 and board[row-1][col] == "O" and (row-1,col) not in discovered :
                queue.append((row-1,col))
                discovered.add((row-1,col))
            if row + 1 < numberOfRows and board[row+1][col] == "O" and (row+1,col) not in discovered :
                queue.append((row+1,col))
                discovered.add((row+1,col))
    return freePathExists

def capture(board,numberOfRows,numberOfCols):
    freePathExists = preProcess(board,numberOfRows,numberOfCols)
    for row in range(numberOfRows):
        for col in range(numberOfCols):
            if board[row][col] == "O" and (row,col) not in freePathExists:
                board[row][col] = "X"
def main():
    numberOfRows = input("enter number of rows in the board")
    board = [[] for _ in range(numberOfRows)]
    for rowNum in range(numberOfRows):
        board[rowNum] = list(raw_input("Enter the XO combination in row %s :"%rowNum))
    capture(board,numberOfRows,len(board[0]))
    for row in board :
        print row
main()


