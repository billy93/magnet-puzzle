import random

M = 6
N = 5


# Function to read board from file
def readBoard(file):
    global M
    global N
    f = open(file, "r")
    lines = f.readlines()

    totalRow = 0
    totalColumn = 0
    positivesRow = []
    negativesRow = []
    positivesColumn = []
    negativesColumn = []
    orientations = []
    workingBoard = []
    for row in range(len(lines)):
        if row == 0:
            totalRow = int(lines[row])
            M = totalRow
        elif row == 1:
            totalColumn = int(lines[row])
            N = totalColumn
            orientations = [[0 for x in range(totalColumn)] for y in range(totalRow)]
            workingBoard = [[0 for x in range(totalColumn)] for y in range(totalRow)]
        elif 2 <= row <= 5:
            rowColumnSize = lines[row].strip().split(' ')
            if row == 2:
                for i in range(len(rowColumnSize)):
                    positivesColumn.append(int(rowColumnSize[i]))
            elif row == 3:
                for i in range(len(rowColumnSize)):
                    negativesColumn.append(int(rowColumnSize[i]))
            elif row == 4:
                for i in range(len(rowColumnSize)):
                    positivesRow.append(int(rowColumnSize[i]))
            elif row == 5:
                for i in range(len(rowColumnSize)):
                    negativesRow.append(int(rowColumnSize[i]))
        elif 6 <= row < (6 + totalRow):
            a = lines[row].strip().split(' ')
            for i, k in enumerate(a[0]):
                orientations[row - 6][i] = k
        elif (6 + totalRow) <= row < (6 + totalRow + totalRow):
            a = lines[row].strip().split(' ')
            for i, k in enumerate(a[0]):
                workingBoard[row - (6 + totalRow)][i] = k
    return positivesRow, negativesRow, positivesColumn, negativesColumn, orientations, workingBoard


# Part A: Representation and display (15 marks)
# Task 1: Initial setup (5 marks)
# Test it
positivesRow, negativesRow, positivesColumn, negativesColumn, orientations, workingBoard = readBoard('config.txt')


# Function to print board
def printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard):
    global M
    global N

    # print('row : '+str(M)+' | column : '+str(N))
    # print('positive column : '+str(len(positivesColumn)))
    print(" + |", end="");
    for p in range(len(positivesColumn)):
        val = positivesColumn[p];
        if val == -1:
            val = 0;

        if val != 0:
            print(" " + str(val) + " |", end="")
        else:
            print("   |", end="")

    print("")

    for i in range(M):
        if i == 0:
            print("---", end="")
            for x in range(len(positivesColumn) + 1):
                print("|---", end="")
            print()
        else:
            print("---", end="")
            for j in range(N):
                print("|", end="")

                if orientations[i][j] == 'L':
                    print("---", end="")
                elif orientations[i][j] == 'R':
                    print("---", end="")
                elif orientations[i][j] == 'T':
                    print("---", end="")
                elif orientations[i][j] == 'B':
                    print("   ", end="")
            print("|---")

        for j in range(N):
            value = " "
            if workingBoard[i][j] != 'E':
                value = workingBoard[i][j] + ""
            pipe = ""
            if j == 0:
                if positivesRow[i] == -1:
                    pipe = "   |"
                else:
                    pipe = " " + str(positivesRow[i]) + " |"
            elif orientations[i][j] == 'L':
                pipe = "|"
            elif orientations[i][j] == 'R':
                pipe = " "
            elif orientations[i][j] == 'T':
                pipe = "|"
            elif orientations[i][j] == 'B':
                pipe = "|"
            print(pipe + " " + value + " ", end="")

        if negativesRow[i] == -1:
            print("|  ")
        else:
            print("| " + str(negativesRow[i]));

        if i == (M - 1):
            print("---", end="");
            for x in range(len(positivesColumn) + 1):
                print("|---", end="")
            print();

    print("   |", end="");
    for p in range(len(negativesColumn)):
        val = negativesColumn[p];
        if negativesColumn[p] == -1:
            val = 0;

        if val != 0:
            print(" " + str(val) + " |", end="")
        else:
            print("   |", end="")
    print(" - ");


# Task 2: Display (10 marks)
# Test it
# printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard)

######################################################
# Part B: Helper functions (25 marks)
# Task 1: Safe placing (10 marks)
def canPlacePole(row, col, pole, workingBoard):
    numrows = len(workingBoard)
    numcols = len(workingBoard[0])

    vals = []
    if row > 0:
        if workingBoard[row - 1][col] != pole:
            vals.append(True)
        else:
            vals.append(False)

    if row + 1 < numrows:
        if workingBoard[row + 1][col] != pole:
            vals.append(True)
        else:
            vals.append(False)

    if col > 0:
        if workingBoard[row][col - 1] != pole:
            vals.append(True)
        else:
            vals.append(False)

    if col + 1 < numcols:
        if workingBoard[row][col + 1] != pole:
            vals.append(True)
        else:
            vals.append(False)

    # if (workingBoard[row - 1][col] != pole) and workingBoard[row][col - 1] != pole and workingBoard[row + 1][
    #     col] != pole and workingBoard[row][col + 1] != pole:
    #     return True
    # else:
    #     return False
    return all(vals)


# Test it
# print(canPlacePole(1, 1, '+', workingBoard))
# print(canPlacePole(2, 3, '-', workingBoard))
# print(canPlacePole(2, 0, '+', workingBoard))


# Task 2: Block orientation (5 marks)
def getBlockOrientation(row, col, orientations):
    resultOrientation = ''
    oppositeRow = 0
    oppositeCol = 0

    if orientations[row][col] == 'T':
        oppositeRow = row
        oppositeCol = row + 1
        resultOrientation = 'TB'
    elif orientations[row][col] == 'B':
        oppositeRow = row - 1
        oppositeCol = row
        resultOrientation = 'TB'
    elif orientations[row][col] == 'R':
        oppositeRow = col
        oppositeCol = col - 1
        resultOrientation = 'LR'
    elif orientations[row][col] == 'L':
        oppositeRow = col
        oppositeCol = col + 1
        resultOrientation = 'LR'

    if oppositeCol < oppositeRow:
        temp = oppositeCol
        oppositeCol = oppositeRow
        oppositeRow = temp

    return resultOrientation, oppositeRow, oppositeCol


# Test it
# resultOrientation, oppositeRow, oppositeCol = getBlockOrientation (5, 2, orientations)
# print (resultOrientation, oppositeRow, oppositeCol)

# Task 3: Pole Count (5 marks)
def poleCount(rowOrCol, index, pole, workingBoard):
    if rowOrCol == 'r':
        count = 0
        for j in range(N):
            if workingBoard[index][j] == pole:
                count += 1
        return count
    elif rowOrCol == 'c':
        count = 0
        for j in range(M):
            if workingBoard[j][index] == pole:
                count += 1
        return count
    return 0


# Test it
# print(poleCount('r', 5, '+', workingBoard))
# print(poleCount('r', 4, '-', workingBoard))
# print(poleCount('c', 4, '-', workingBoard))


# Task 4: Random Magnetic Pole Distribution (5 marks)
def randomPoleFlip(alist, percentage, flipValue):
    if percentage <= 1:
        percentage = percentage * 100
    numberElementToFlip = len(alist) * percentage / 100

    sample = random.sample(list(enumerate(alist)), int(numberElementToFlip))

    for s in sample:
        alist[s[0]] = flipValue
    return alist


# Test it
# print(randomPoleFlip([1,2,3,4,5,6,7,8,9,10], 10, -1))

######################################################
# Part C: Board Generation Functions (30 marks)

# Task 1: Orientations generation (10 marks)
def orientationsGenerator(M, N):
    initMatrix = [[0 for x in range(N)] for y in range(M)]

    # initMatrix = [
    #     ['L', 'R', 'T', 'T', 'T'],
    #     ['L', 'R', 'B', 'B', 'B'],
    #     ['T', 'T', 'T', 'T', 'T'],
    #     ['B', 'B', 'B', 'B', 'B']
    # ]

    #  initMatrix = [
    #      ['L', 'R', 'L', 'R', 'T'],
    #      ['L', 'R', 'T', 'T', 'B'],
    #      ['L', 'R', 'B', 'B', 'T'],
    #      ['L', 'R', 'L', 'R', 'B']
    # ]

    first = 'T'
    for i in range(M):
        for j in range(N):
            initMatrix[i][j] = first
        if first == 'T':
            first = 'B'
        elif first == 'B':
            first = 'T'

    # positivesColumn = [-1, -1, -1, -1, -1]
    # positivesRow = [-1, -1, -1, -1]
    # negativesColumn = [-1, -1, -1, -1, -1]
    # negativesRow = [-1, -1, -1, -1]
    # workingBoard = [
    #     ['E', 'E', 'E', 'E', 'E'],
    #     ['E', 'E', 'E', 'E', 'E'],
    #     ['E', 'E', 'E', 'E', 'E'],
    #     ['E', 'E', 'E', 'E', 'E']
    # ]
    # printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, initMatrix, workingBoard)
    # initMatrix = shuffle(initMatrix)
    # printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, initMatrix, workingBoard)

    for i in range(1000):
        initMatrix = shuffle(initMatrix)
        # printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, initMatrix, workingBoard)

    return initMatrix


# Used in orientationGenerator to 1000 times shuffle matrix
def shuffle(initMatrix):
    row = random.randint(0, M - 1)
    column = random.randint(0, N - 1)

    # row = 3
    # column = 3
    # Debug selected row and column to shuffle
    resultOrientation, oppositeRow, oppositeCol = getBlockOrientation(row, column, initMatrix)
    # print("ROW : " + str(row) + " | COLUMN : " + str(row))
    # print("resultOrientation : " + resultOrientation)
    # print("oppositeRow : " + str(oppositeRow))
    # print("oppositeCol : " + str(oppositeCol))

    if resultOrientation == 'TB':
        if column == 0:
            # check right block
            resultOrientation2, oppositeRow2, oppositeCol2 = getBlockOrientation(oppositeRow, column + 1, initMatrix)
            if resultOrientation == 'TB' and resultOrientation2 == 'TB' and oppositeRow == oppositeRow2 and oppositeCol == oppositeCol2:
                initMatrix[oppositeRow][column] = 'L'
                initMatrix[oppositeCol][column] = 'L'
                initMatrix[oppositeRow2][column + 1] = 'R'
                initMatrix[oppositeCol2][column + 1] = 'R'
        elif column > 0:
            # check left block
            resultOrientation2, oppositeRow2, oppositeCol2 = getBlockOrientation(oppositeRow, column - 1, initMatrix)
            if resultOrientation == 'TB' and resultOrientation2 == 'TB' and oppositeRow == oppositeRow2 and oppositeCol == oppositeCol2:
                initMatrix[oppositeRow][column] = 'R'
                initMatrix[oppositeCol][column] = 'R'
                initMatrix[oppositeRow2][column - 1] = 'L'
                initMatrix[oppositeCol2][column - 1] = 'L'
    elif resultOrientation == 'LR':
        if row == 0:
            # check bottom block
            resultOrientation2, oppositeRow2, oppositeCol2 = getBlockOrientation(row + 1, oppositeRow, initMatrix)
            if resultOrientation == 'LR' and resultOrientation2 == 'LR' and oppositeRow == oppositeRow2 and oppositeCol == oppositeCol2:
                initMatrix[row][oppositeRow] = 'T'
                initMatrix[row][oppositeCol] = 'T'
                initMatrix[row + 1][oppositeRow2] = 'B'
                initMatrix[row + 1][oppositeCol2] = 'B'
        elif row > 0:
            # check top block
            resultOrientation2, oppositeRow2, oppositeCol2 = getBlockOrientation(row - 1, oppositeRow, initMatrix)
            if resultOrientation == 'LR' and resultOrientation2 == 'LR' and oppositeRow == oppositeRow2 and oppositeCol == oppositeCol2:
                initMatrix[row][oppositeRow] = 'B'
                initMatrix[row][oppositeCol] = 'B'
                initMatrix[row - 1][oppositeRow2] = 'T'
                initMatrix[row - 1][oppositeCol2] = 'T'

    # print("resultOrientation2 : " + resultOrientation2)
    # print("oppositeRow2 : " + str(oppositeRow2))
    # print("oppositeCol2 : " + str(oppositeCol2))

    return initMatrix


# Test it
# M = 4
# N = 5
# print(orientationsGenerator(M, N))


# Task 2: Filling board with magnets (10 marks)
def fillWithMagnets(orientations):
    global N
    global M

    workingBoard = [[0 for x in range(N)] for y in range(M)]
    for i in range(M):
        for j in range(N):
            resultOrientation, oppositeRow, oppositeCol = getBlockOrientation(i, j, orientations)
            # print("resultOrientation : " + resultOrientation)
            # print("oppositeRow : " + str(oppositeRow))
            # print("oppositeCol : " + str(oppositeCol))
            # canPlacePole(i, j, '+', workingBoard)

            if workingBoard[i][j] == 0:
                if orientations[i][j] == 'L':
                    if canPlacePole(i, j, '+', workingBoard):
                        workingBoard[i][j] = '+'
                        if canPlacePole(i, j + 1, '-', workingBoard):
                            workingBoard[i][j + 1] = '-'
                elif orientations[i][j] == 'T':
                    if canPlacePole(i, j, '+', workingBoard):
                        workingBoard[i][j] = '+'
                        if canPlacePole(i + 1, j, '-', workingBoard):
                            workingBoard[i + 1][j] = '-'
    for i in range(M):
        for j in range(N):
            if workingBoard[i][j] == 0:
                workingBoard[i][j] = 'E'
    return workingBoard


# Test fill with magnets
# positivesColumn = [-1, -1, -1, -1, -1]
# negativesColumn = [-1, -1, -1, -1, -1]
# positivesRow = [-1, -1, -1, -1]
# negativesRow = [-1, -1, -1, -1]
# M = 4
# N = 5
# orientations = orientationsGenerator(M, N)
# workingBoard = fillWithMagnets(orientations)
# printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard)

# Task 3: Generating random new board (10 marks)
def randomNewBoard(M, N):
    orientations = orientationsGenerator(M, N)
    workingBoard = fillWithMagnets(orientations)

    # Replace empty board with X
    for i in range(M):
        for j in range(N):
            if workingBoard[i][j] == 'E':
                workingBoard[i][j] = 'X'

    # Get Count put in array
    positivesRow = []
    negativesRow = []
    negativesColumn = []
    positivesColumn = []
    for i in range(M):
        positivesRow.append(poleCount('r', i, '+', workingBoard))
        negativesRow.append(poleCount('r', i, '-', workingBoard))

    for j in range(N):
        positivesColumn.append(poleCount('c', j, '+', workingBoard))
        negativesColumn.append(poleCount('c', j, '-', workingBoard))

    # Random 50% flip
    randomPoleFlip(positivesRow, 50, -1)
    randomPoleFlip(negativesRow, 50, -1)
    randomPoleFlip(negativesColumn, 50, -1)
    randomPoleFlip(positivesColumn, 50, -1)

    return positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard


# Test it
# M = 6
# N = 5
# positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard = randomNewBoard(M, N)
# printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard)

######################################################
# Part D: Decomposition, Variable names and code Documentation (10 marks)



# Assignment 2
# Part A: Helper functions (10 marks)
# Task 1: Converting a set into a board (5 Marks)
def setToBoard(set, orientations):
    global M
    global N
    workingBoard = [[0 for x in range(N)] for y in range(M)]
    for x in range(M):
        for y in range(N):
            workingBoard[x][y] = 'E'

    # for dataSet in range(len(set)):
    dataSet = 0

    try:
        for x in range(M):
            for y in range(N):
                if workingBoard[x][y] == 'E':
                    if set[dataSet] == 0:
                        if orientations[x][y] == 'L':
                            workingBoard[x][y] = '+'
                            workingBoard[x][y + 1] = '-'
                            dataSet += 1
                            if dataSet >= len(set):
                                raise StopIteration
                        elif orientations[x][y] == 'T':
                            workingBoard[x][y] = '+'
                            workingBoard[x + 1][y] = '-'
                            dataSet += 1
                            if dataSet >= len(set):
                                raise StopIteration
                    elif set[dataSet] == 1:
                        if orientations[x][y] == 'L':
                            workingBoard[x][y] = '-'
                            workingBoard[x][y + 1] = '+'
                            dataSet += 1
                            if dataSet >= len(set):
                                raise StopIteration
                        elif orientations[x][y] == 'T':
                            workingBoard[x][y] = '-'
                            workingBoard[x + 1][y] = '+'
                            dataSet += 1
                            if dataSet >= len(set):
                                raise StopIteration
                    elif set[dataSet] == 2:
                        if orientations[x][y] == 'L':
                            workingBoard[x][y] = 'X'
                            workingBoard[x][y + 1] = 'X'
                            dataSet += 1
                            if dataSet >= len(set):
                                raise StopIteration
                        elif orientations[x][y] == 'T':
                            workingBoard[x][y] = 'X'
                            workingBoard[x + 1][y] = 'X'
                            dataSet += 1
                            if dataSet >= len(set):
                                raise StopIteration
    except StopIteration:
        pass
    return workingBoard

# Test it
# M = 6
# N - 5
# positivesColumn = [-1, -1, -1, -1, -1]
# negativesColumn = [-1, -1, -1, -1, -1]
# positivesRow = [-1, -1, -1, -1, -1, -1]
# negativesRow = [-1, -1, -1, -1, -1, -1]
# orientations = [['T', 'L', 'R', 'L', 'R'],
#                 ['B', 'T', 'T', 'L', 'R'],
#                 ['T', 'B', 'B', 'T', 'T'],
#                 ['B', 'L', 'R', 'B', 'B'],
#                 ['L', 'R', 'L', 'R', 'T'],
#                 ['L', 'R', 'L', 'R', 'B']]
# printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, orientations)
# set=[0,1,1,0]
# workingBoard= setToBoard(set,orientations)
# print("###########################################")
# printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard)
# set =[0,2,0,2,1,0,2]
# workingBoard= setToBoard(set,orientations)
# print("###########################################")
# printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations,
# workingBoard)

# Task 2: Check solution (5 marks)
def isSolution(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard):
    check = True
    for x in range(M):
        for y in range(N):
            if workingBoard[x][y] == '+':
                # down
                try:
                    if (x+1) <= M:
                        if workingBoard[x+1][y] == '+':
                            check = False
                except:
                    pass

                # right
                try:
                    if (y + 1) <= N:
                        if workingBoard[x][y+1] == '+':
                            check = False
                except:
                    pass

                # up
                try:
                    if (x - 1) >= 0:
                        if workingBoard[x-1][y] == '+':
                            check = False
                except:
                    pass

                # left
                try:
                    if (y - 1) >= 0:
                        if workingBoard[x][y-1] == '+':
                            check = False
                except:
                    print("Error")
                    pass

            elif workingBoard[x][y] == '-':
                # down
                try:
                    if (x + 1) <= M:
                        if workingBoard[x+1][y] == '-':
                            check = False
                except:
                    pass

                # right
                try:
                    if (y + 1) <= N:
                        if workingBoard[x][y+1] == '-':
                            check = False
                except:
                    pass

                # up
                try:
                    if (x - 1) >= 0:
                        if workingBoard[x-1][y] == '-':
                            check = False
                except:
                    pass

                # left
                try:
                    if (y - 1) >= 0:
                        if workingBoard[x][y-1] == '-':
                          check = False
                except:
                    pass

    if check:
        for x in range(M):
            if positivesRow[x] != -1:
                count = poleCount('r', x, '+', workingBoard)
                if count == 0:
                    count = -1
                if positivesRow[x] != count:
                    check = False

            if negativesRow[x] != -1:
                negativeCount = poleCount('r', x, '-', workingBoard)
                if negativeCount == 0:
                    negativeCount = -1
                if negativesRow[x] != negativeCount:
                    check = False

        for y in range(N):
            if positivesColumn[y] != -1:
                count = poleCount('c', y, '+', workingBoard)
                if count == 0:
                    count = -1
                if positivesColumn[y] != count:
                    check = False

            if negativesColumn[y] != -1:
                negativeCount = poleCount('c', y, '-', workingBoard)
                if negativeCount == 0:
                    negativeCount = -1
                if negativesColumn[y] != negativeCount:
                    check = False
    return check

# Test it
# M = 2
# N = 3
# positivesColumn= [1,1,1]
# negativesColumn= [1,1,1]
# positivesRow= [-1,-1]
# negativesRow= [-1,-1]
# orientations= [['L', 'R', 'T'],
#                ['L', 'R', 'B']]
# workingBoard = [
#             ['+', '-', '-'],
#             ['-', '+', '+']
# ]
# printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard)
# print(isSolution(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard))
#
# workingBoard = [
#     ['+', '-', '+'],
#     ['-', '+', '-']
# ]
# printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard)
# print(isSolution(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, workingBoard))

def backtrack(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, partial):
    partial = [[0 for x in range(N)] for y in range(M)]
    for x in range(M):
        for y in range(N):
            partial[x][y] = 'E'

    if not solveBacktrack(partial, 0, 0, positivesColumn, negativesColumn, positivesRow, negativesRow, partial):
        print("Cannot solve")
        return

    return partial

def solveBacktrack(board, row, col, positivesColumn, negativesColumn, positivesRow, negativesRow, orientations):

    return False

# // Main function to solve the Bipolar Magnets puzzle
# 	private static boolean solveMagnetPuzzle(char board[][], int row, int col,
# 				int top[], int left[], int bottom[], int right[], char str[][])
# 	{
# 		// if we have reached last cell
# 		if (row >= M - 1 && col >= N - 1)
# 		{
# 			return validateConfiguration(board, top, left, bottom, right);
# 		}
#
# 		// if last column of current row is already processed,
# 		// go to next row, first column
# 		if (col >= N)
# 		{
# 			col = 0;
# 			row = row + 1;
# 		}
#
# 		// if current cell contains 'R' or 'B' (end of horizontal
# 		// or vertical slot) recur for next cell
# 		if (str[row][col] == 'R' || str[row][col] == 'B')
# 		{
# 			if (solveMagnetPuzzle(board, row, col + 1, top,
# 					left, bottom, right, str))
# 				return true;
# 		}
#
# 		// if horizontal slot contains L and R
# 		if (str[row][col] == 'L' && str[row][col + 1] == 'R')
# 		{
# 			// put ('+', '-') pair and recur
# 			if (isSafe(board, row, col, '+', top, left, bottom, right) &&
# 				isSafe(board, row, col + 1, '-', top, left, bottom, right))
# 			{
# 				board[row][col] = '+';
# 				board[row][col + 1] = '-';
#
# 				if (solveMagnetPuzzle(board, row, col + 2,
# 						top, left, bottom, right, str))
# 					return true;
#
# 				// if it doesn't lead to a solution, backtrack
# 				board[row][col] = 'X';
# 				board[row][col + 1] = 'X';
# 			}
#
# 			// put ('-', '+') pair and recur
# 			if (isSafe(board, row, col, '-', top, left, bottom, right) &&
# 				isSafe(board, row, col + 1, '+', top, left, bottom, right))
# 			{
# 				board[row][col] = '-';
# 				board[row][col + 1] = '+';
#
# 				if (solveMagnetPuzzle(board, row, col + 2,
# 						top, left, bottom, right, str))
# 					return true;
#
# 				// if it doesn't lead to a solution, backtrack
# 				board[row][col] = 'X';
# 				board[row][col + 1] = 'X';
# 			}
# 		}
#
# 		// if vertical slot contains T and B
# 		if (str[row][col] == 'T' && str[row + 1][col] == 'B')
# 		{
# 			// put ('+', '-') pair and recur
# 			if (isSafe(board, row, col, '+', top, left, bottom, right) &&
# 				isSafe(board, row + 1, col, '-', top, left, bottom, right))
# 			{
# 				board[row][col] = '+';
# 				board[row + 1][col] = '-';
#
# 				if (solveMagnetPuzzle(board, row, col + 1,
# 						top, left, bottom, right, str))
# 					return true;
#
# 				// if it doesn't lead to a solution, backtrack
# 				board[row][col] = 'X';
# 				board[row + 1][col] = 'X';
# 			}
#
# 			// put ('-', '+') pair and recur
# 			if (isSafe(board, row, col, '-', top, left, bottom, right) &&
# 				isSafe(board, row + 1, col, '+', top, left, bottom, right))
# 			{
# 				board[row][col] = '-';
# 				board[row + 1][col] = '+';
#
# 				if (solveMagnetPuzzle(board, row, col + 1,
# 						top, left, bottom, right, str))
# 					return true;
#
# 				// if it doesn't lead to a solution, backtrack
# 				board[row][col] = 'X';
# 				board[row + 1][col] = 'X';
# 			}
# 		}
#
# 		// ignore current cell and recur
# 		if (solveMagnetPuzzle(board, row, col + 1,
# 				top, left, bottom, right, str))
# 			return true;
#
# 		// if no solution is possible, return false
# 		return false;
# 	}
#
# 	public static void solveMagnetPuzzle(int top[], int left[], int bottom[],
# 							int right[], char str[][])
# 	{
# 		// to store result
# 		char board[][] = new char[M][N];
#
# 		// initalize all cells by 'X'
# 		for (int i = 0; i < M; i++)
# 			Arrays.fill(board[i], 'X');
#
# 		// start from (0, 0) cell
# 		if (!solveMagnetPuzzle(board, 0, 0, top, left, bottom, right, str))
# 		{
# 			System.out.println("Solution does not exist");
# 			return;
# 		}
#
# 		// print result if given configuration is solvable
# 		printSolution(board);
# 	}

# M = 4
# N - 5
# positivesColumn= [2, 1, 1, -1, -1]
# negativesColumn= [1, -1, -1, 2, 1]
# positivesRow= [2, -1, -1, 1]
# negativesRow= [1, 3, -1, 1]
# orientations= [['T', 'L', 'R', 'L', 'R'],
#                ['B', 'L', 'R', 'L', 'R'],
#                ['L', 'R', 'L', 'R', 'T'],
#                ['L', 'R', 'L', 'R', 'B']
#               ]
#
# printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, orientations)
# print("#############################################")
# partial=[]
# solution = []
# solution = backtrack(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, partial)
# printBoard(positivesColumn, negativesColumn, positivesRow, negativesRow, orientations, solution)