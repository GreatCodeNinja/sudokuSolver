#############
# TODO list #
#############
# Naked Trips 
# X-Wing
# Unique Rectangle
# Hidden pair
# Hidden trips
#############


puzzle = [
        [0,4,3,0,0,2,6,0,0],
        [9,0,0,0,0,8,0,0,0],
        [6,0,0,0,0,0,0,0,9],
        [0,0,0,3,0,4,8,7,0],
        [0,0,0,0,0,0,0,0,0],
        [3,6,0,8,0,1,0,5,0],
        [5,0,0,2,0,0,0,6,0],
        [0,0,0,9,0,7,2,0,0],
        [0,0,4,0,0,0,0,0,0]
        ]

candidates =[
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]]
        ]

notCandidates =[
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]]
        ]

pairs =[
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]]
        ]

zeroCounter = 0

#print([i[3] for i in puzzle])
def findCandidates():
    zeroCounter = 0
    clearCandidates()
    for i in range(9):
        for j in range(9):           
            if puzzle[i][j] == 0:
                sq = findMySquare(i, j)
                zeroCounter += 1
                for k in range(9):
                    if k+1 not in puzzle[i] and k+1 not in [x[j] for x in puzzle] and k+1 not in [b for a in sq for b in a]:
                        if k+1 not in candidates[i][j] and k+1 not in notCandidates[i][j]:
                            candidates[i][j].append(k+1)
    return zeroCounter

def clearCandidates():
    for a in range(9):
        for b in range(9):
            candidates[a][b].clear()

def solve():
    for i in range(9):
        for j in range(9):
            if len(candidates[i][j]) == 1:
                puzzle[i][j] = candidates[i][j][0]
                del candidates[i][j][0]
    clearCandidates()

def findPairs():
    for i in range(9):
        for j in range(9):
            if len(candidates[i][j]) == 2:
                pairs[i][j] = candidates[i][j]


#findMySquare
def findMySquare(a, b):
    if a >= 0 and a <= 2:
        if b >=0 and b <= 2:
            return [x[:3] for x in puzzle[:3]]
        elif b >= 3 and b <= 5:
            return [x[3:6] for x in puzzle[:3]]
        else:
            return [x[6:] for x in puzzle[:3]]
    elif a >=3 and a <=5:
        if b >=0 and b <= 2:
            return [x[:3] for x in puzzle[3:6]]
        elif b >= 3 and b <= 5:
            return [x[3:6] for x in puzzle[3:6]]
        else:
            return [x[6:] for x in puzzle[3:6]]
    else:
        if b >=0 and b <= 2:
            return [x[:3] for x in puzzle[6:]]
        elif b >= 3 and b <= 5:
            return [x[3:6] for x in puzzle[6:]]
        else:
            return [x[6:] for x in puzzle[6:]]

#printIt
def printIt(x):
    for i in range(len(x)):
        print(x[i])

#insertIntoRows
def insertIntoRows(row,column,value):
    puzzle[row][column] = value
    candidates[row][column].clear()
    return


#findPosAndInsertValue
def findPosAndInsertValue(box,row,column,value):
    if box == 1:
        puzzle[row][column] = value
        candidates[row][column].clear()
        return
    elif box == 2:
        puzzle[row][column + 3] = value
        candidates[row][column + 3].clear()
        return
    elif box == 3:
        puzzle[row][column + 6] = value
        candidates[row][column + 6].clear()
        return
    elif box == 4:
        puzzle[row + 3][column] = value
        candidates[row + 3][column].clear()
        return
    elif box == 5:
        puzzle[row + 3][column + 3] = value
        candidates[row + 3][column + 3].clear()
        return
    elif box == 6:
        puzzle[row + 3][column + 6] = value
        candidates[row + 3][column + 6].clear()
        return
    elif box == 7:
        puzzle[row + 6][column] = value
        candidates[row + 6][column].clear()
        return
    elif box == 8:
        puzzle[row + 6][column + 3] = value
        candidates[row + 6][column + 3].clear()
        return
    elif box == 9:
        puzzle[row + 6][column + 6] = value
        candidates[row + 6][column + 6].clear()
        return
    else:
        print('Not a valid box!!!')

#ifOnlyOneInColumn
def ifOnlyOneInColumn(columns):
    z3 = 10
    x3 = 10

    k = 1
    for i in columns:
        for j in range(1,10):
            if sum(x.count(j) for x in i) == 1:
                #print('There is', sum(x.count(j) for x in i),str(j) + ' in column',k)
                for x in i:
                    if j in x:
                        z3 = i.index(x)
                        x3 = columns.index(i)
                        insertIntoRows(z3,x3,j)
        k += 1

    zeroCounter = findCandidates()
########################################################################################
#ifOnlyOneInRow
def ifOnlyOneInRow(rows):
    z2 = 10
    x2 = 10

    k = 1
    for i in rows:
        for j in range(1,10):
            if sum(x.count(j) for z in i for x in z) == 1:
                #print('There is',sum(x.count(j) for z in i for x in z),str(j) + ' in row',k)
                for z in i:
                    for x in z:
                        if j in i[i.index(z)][z.index(x)]:
                            z2 = i.index(z)
                            x2 = z.index(x)
                            insertIntoRows(k-1, x2, j)

        k += 1
    zeroCounter = findCandidates()
##########################################################################################
#ifOnlyOneInBox
def ifOnlyOneInBox(boxes):
    k = 1
    
    z1 = 10
    x1 = 10

    for i in boxes:
        for j in range(1,10):
            if sum(x.count(j) for z in i for x in z) == 1:
                #print('There is',sum(x.count(j) for z in i for x in z),str(j) + ' in box',k)
                for z in i:
                    for x in z:
                        if j in i[i.index(z)][z.index(x)]:
                            z1 = i.index(z)
                            x1 = z.index(x)
                            #print(i.index(z),z.index(x))
                            findPosAndInsertValue(k,z1,x1,j)
                            #k=box, z1=row, x1=column
        k += 1
    zeroCounter = findCandidates()
########################################
#candidateTrimmingCol
def candidateTrimmingCol(boxes):
    boxNumber = 1

    for i in boxes:
        c1 = [x[0] for x in i[:]]
        c2 = [x[1] for x in i[:]]
        c3 = [x[2] for x in i[:]]
        
        col1 = [item for sublist in c1 for item in sublist]
        col2 = [item for sublist in c2 for item in sublist]
        col3 = [item for sublist in c3 for item in sublist]
        #print('col1',col1,'\ncol2',col2,'\ncol2',col3)
        for j in range(1,10):
            if j in col1 and j not in col2 and j not in col3:
                #print(j,'is in',i[0])
                #remove from candidates and insert into not candidates
                if boxNumber == 1:
                    #remove j from candidates[3:][0]
                    for counter in range(3,9):
                        if j in candidates[counter][0]:
                            candidates[counter][0].remove(j)
                        notCandidates[counter][0].append(j)
                elif boxNumber == 2:
                    #remove j from candidates[3:][3]
                    for counter in range(3,9):
                        if j in candidates[counter][3]:
                            candidates[counter][3].remove(j)
                        notCandidates[counter][3].append(j)
                elif boxNumber == 3:
                    #remove j from candidates[3:][6]
                    for counter in range(3,9):
                        if j in candidates[counter][6]:
                            candidates[counter][6].remove(j)
                        notCandidates[counter][6].append(j)
                elif boxNumber == 4:
                    #remove j from candidates[:3][0] and form candidates[6:][0]
                    for counter in range(3):
                        if j in candidates[counter][0]:
                            candidates[counter][0].remove(j)
                        notCandidates[counter][0].append(j)
                    for counter in range(6,9):
                        if j in candidates[counter][0]:
                            candidates[counter][0].remove(j)
                        notCandidates[counter][0].append(j)
                elif boxNumber == 5:
                    #remove j from candidates[:3][3] and candidates[6:][3]
                    for counter in range(3):
                        if j in candidates[counter][3]:
                            candidates[counter][3].remove(j)
                        notCandidates[counter][3].append(j)
                    for counter in range(6,9):
                        if j in candidates[counter][3]:
                            candidates[counter][3].remove(j)
                        notCandidates[counter][3].append(j)
                elif boxNumber == 6:
                    #remove j from candidates[:3][6] and candidates[6:][6]
                    for counter in range(3):
                        if j in candidates[counter][6]:
                            candidates[counter][6].remove(j)
                        notCandidates[counter][6].append(j)
                    for counter in range(6,9):
                        if j in candidates[counter][6]:
                            candidates[counter][6].remove(j)
                        notCandidates[counter][6].append(j)
                elif boxNumber == 7:
                    #remove j from candidates[:6][0]
                    for counter in range(6):
                        if j in candidates[counter][0]:
                            candidates[counter][0].remove(j)
                        notCandidates[counter][0].append(j)
                elif boxNumber == 8:
                    #remove j from candidates[:6][3]
                    for counter in range(6):
                        if j in candidates[counter][3]:
                            candidates[counter][3].remove(j)
                        notCandidates[counter][3].append(j)
                elif boxNumber == 9:
                    #remove j from candidates[:6][6]
                    for counter in range(6):
                        if j in candidates[counter][6]:
                            candidates[counter][6].remove(j)
                        notCandidates[counter][6].append(j)
            elif j in col2 and j not in col1 and j not in col3:
                #print(j,'is in',i[0])
                #remove from candidates and insert into not candidates
                if boxNumber == 1:
                    #remove j from candidates[3:][0]
                    for counter in range(3,9):
                        if j in candidates[counter][1]:
                            candidates[counter][1].remove(j)
                        notCandidates[counter][1].append(j)
                elif boxNumber == 2:
                    #remove j from candidates[3:][3]
                    for counter in range(3,9):
                        if j in candidates[counter][4]:
                            candidates[counter][4].remove(j)
                        notCandidates[counter][4].append(j)
                elif boxNumber == 3:
                    #remove j from candidates[3:][6]
                    for counter in range(3,9):
                        if j in candidates[counter][7]:
                            candidates[counter][7].remove(j)
                        notCandidates[counter][7].append(j)
                elif boxNumber == 4:
                    #remove j from candidates[:3][0] and form candidates[6:][0]
                    for counter in range(3):
                        if j in candidates[counter][1]:
                            candidates[counter][1].remove(j)
                        notCandidates[counter][1].append(j)
                    for counter in range(6,9):
                        if j in candidates[counter][1]:
                            candidates[counter][1].remove(j)
                        notCandidates[counter][1].append(j)
                elif boxNumber == 5:
                    #remove j from candidates[:3][3] and candidates[6:][3]
                    for counter in range(3):
                        if j in candidates[counter][4]:
                            candidates[counter][4].remove(j)
                        notCandidates[counter][4].append(j)
                    for counter in range(6,9):
                        if j in candidates[counter][4]:
                            candidates[counter][4].remove(j)
                        notCandidates[counter][4].append(j)
                elif boxNumber == 6:
                    #remove j from candidates[:3][6] and candidates[6:][6]
                    for counter in range(3):
                        if j in candidates[counter][7]:
                            candidates[counter][7].remove(j)
                        notCandidates[counter][7].append(j)
                    for counter in range(6,9):
                        if j in candidates[counter][7]:
                            candidates[counter][7].remove(j)
                        notCandidates[counter][7].append(j)
                elif boxNumber == 7:
                    #remove j from candidates[:6][0]
                    for counter in range(6):
                        if j in candidates[counter][1]:
                            candidates[counter][1].remove(j)
                        notCandidates[counter][1].append(j)
                elif boxNumber == 8:
                    #remove j from candidates[:6][3]
                    for counter in range(6):
                        if j in candidates[counter][4]:
                            candidates[counter][4].remove(j)
                        notCandidates[counter][4].append(j)
                elif boxNumber == 9:
                    #remove j from candidates[:6][6]
                    for counter in range(6):
                        if j in candidates[counter][7]:
                            candidates[counter][7].remove(j)
                        notCandidates[counter][7].append(j)
            elif j in col3 and j not in col1 and j not in col2:
               #print(j,'is in',i[0])
               #remove from candidates and insert into not candidates
                if boxNumber == 1:
                   #remove j from candidates[3:][0]
                    for counter in range(3,9):
                        if j in candidates[counter][2]:
                            candidates[counter][2].remove(j)
                        notCandidates[counter][2].append(j)
                elif boxNumber == 2:
                    #remove j from candidates[3:][3]
                    for counter in range(3,9):
                        if j in candidates[counter][5]:
                            candidates[counter][5].remove(j)
                        notCandidates[counter][5].append(j)
                elif boxNumber == 3:
                    #remove j from candidates[3:][6]
                    for counter in range(3,9):
                        if j in candidates[counter][8]:
                            candidates[counter][8].remove(j)
                        notCandidates[counter][8].append(j)
                elif boxNumber == 4:
                    #remove j from candidates[:3][0] and form candidates[6:][0]
                    for counter in range(3):
                        if j in candidates[counter][2]:
                            candidates[counter][2].remove(j)
                        notCandidates[counter][2].append(j)
                    for counter in range(6,9):
                        if j in candidates[counter][2]:
                            candidates[counter][2].remove(j)
                        notCandidates[counter][2].append(j)
                elif boxNumber == 5:
                    #remove j from candidates[:3][3] and candidates[6:][3]
                    for counter in range(3):
                        if j in candidates[counter][5]:
                            candidates[counter][5].remove(j)
                        notCandidates[counter][5].append(j)
                    for counter in range(6,9):
                        if j in candidates[counter][5]:
                            candidates[counter][5].remove(j)
                        notCandidates[counter][5].append(j)
                elif boxNumber == 6:
                    #remove j from candidates[:3][6] and candidates[6:][6]
                    for counter in range(3):
                        if j in candidates[counter][8]:
                            candidates[counter][8].remove(j)
                        notCandidates[counter][8].append(j)
                    for counter in range(6,9):
                        if j in candidates[counter][8]:
                            candidates[counter][8].remove(j)
                        notCandidates[counter][8].append(j)
                elif boxNumber == 7:
                    #remove j from candidates[:6][0]
                    for counter in range(6):
                        if j in candidates[counter][2]:
                            candidates[counter][2].remove(j)
                        notCandidates[counter][2].append(j)
                elif boxNumber == 8:
                    #remove j from candidates[:6][3]
                    for counter in range(6):
                        if j in candidates[counter][5]:
                            candidates[counter][5].remove(j)
                        notCandidates[counter][5].append(j)
                elif boxNumber == 9:
                    #remove j from candidates[:6][6]
                    for counter in range(6):
                        if j in candidates[counter][8]:
                            candidates[counter][8].remove(j)
                        notCandidates[counter][8].append(j)

        boxNumber += 1
    zeroCounter = findCandidates()


#################################################################################################
#candidateTrimmingRow
def candidateTrimmingRow(boxes):
    boxNumber = 1

    for i in boxes:
        r1 = [item for sublist in i[0] for item in sublist]
        r2 = [item for sublist in i[1] for item in sublist]
        r3 = [item for sublist in i[2] for item in sublist]

        #print('r1',r1,'\nr2',r2,'\nr3',r3)

        for j in range(1,10):
            #print('Checking for',j,'in',i[0],'\n',i[1],'\n',i[2],'in box',boxNumber)
            #r1 = [item for sublist in i[0] for item in sublist]
            #r2 = [item for sublist in i[1] for item in sublist]
            #r3 = [item for sublist in i[2] for item in sublist]
            
            
            if j in r1 and j not in r2 and j not in r3:
                #print(j,'is in',i[0])
                #remove from candidates and insert into not candidates
                if boxNumber == 1:
                    #remove j from candidates[0][3:]
                    for counter in range(3,9):
                        if j in candidates[0][counter]:
                            candidates[0][counter].remove(j)
                        notCandidates[0][counter].append(j)
                elif boxNumber == 2:
                    #remove j from candidates[0][:3] and candidates[0][6:]
                    for counter in range(3):
                        if j in candidates[0][counter]:
                            candidates[0][counter].remove(j)
                        notCandidates[0][counter].append(j)
                    for counter in range(6,9):
                        if j in candidates[0][counter]:
                            candidates[0][counter].remove(j)
                        notCandidates[0][counter].append(j)
                elif boxNumber == 3:
                    #remove j from candidates[0][:6]
                    for counter in range(6):
                        if j in candidates[0][counter]:
                            candidates[0][counter].remove(j)
                        notCandidates[0][counter].append(j)
                elif boxNumber == 4:
                    #remove j from candidates[3][3:]
                    for counter in range (3,9):
                        if j in candidates[3][counter]:
                            candidates[3][counter].remove(j)
                        notCandidates[3][counter].append(j)
                elif boxNumber == 5:
                    #remove j from candidates[3][:3] and candidates[3][6:]
                    for counter in range(3):
                        if j in candidates[3][counter]:
                            candidates[3][counter].remove(j)
                        notCandidates[3][counter].append(j)
                    for counter in range(6,9):
                        if j in candidates[3][counter]:
                            candidates[3][counter].remove(j)
                        notCandidates[3][counter].append(j)
                elif boxNumber == 6:
                    #remove j from candidates[3][:6]
                    for counter in range(6):
                        if j in candidates[3][counter]:
                            candidates[3][counter].remove(j)
                        notCandidates[3][counter].append(j)
                elif boxNumber == 7:
                    #remove j from candidates[6][3:]
                    for counter in range(3,9):
                        if j in candidates[6][counter]:
                            candidates[6][counter].remove(j)
                        notCandidates[6][counter].append(j)
                elif boxNumber == 8:
                    #remove j from candidates[6][:3] and candidates[6][6:]
                    for counter in range(3):
                        if j in candidates[6][counter]:
                            candidates[6][counter].remove(j)
                        notCandidates[6][counter].append(j)
                    for counter in range(6,9):
                        if j in candidates[6][counter]:
                            candidates[6][counter].remove(j)
                        notCandidates[6][counter].append(j)
                elif boxNumber == 9:
                    #remove j from candidates[6][:6]
                    for counter in range(6):
                        if j in candidates[6][counter]:
                            candidates[6][counter].remove(j)
                        notCandidates[6][counter].append(j)
            elif j in r2 and j not in r1 and j not in r3:
                #remove from candidates and insert into not candidates
                if boxNumber == 1:
                    #remove j from candidates[1][3:]
                    for counter in range(3,9):
                        if j in candidates[1][counter]:
                            candidates[1][counter].remove(j)
                        notCandidates[1][counter].append(j)
                elif boxNumber == 2:
                    #remove j from candidates[1][0:3] and candidates[1][6:]
                    for counter in range(3):
                        if j in candidates[1][counter]:
                            candidates[1][counter].remove(j)
                        notCandidates[1][counter].append(j)
                    for counter in range(6,9):
                        if j in candidates[1][counter]:
                            candidates[1][6:].remove(j)
                        notCandidates[1][6:].append(j)
                elif boxNumber == 3:
                    #remove j from candidates[1][:6]
                    for counter in range(6):
                        if j in candidates[1][counter]:
                            candidates[1][counter].remove(j)
                        notCandidates[1][counter].append(j)
                elif boxNumber == 4:
                    #remove j from candidates[4][3:]
                    for counter in range(3,9):
                        if j in candidates[4][counter]:
                            candidates[4][counter].remove(j)
                        notCandidates[4][counter].append(j)
                elif boxNumber == 5:
                    #remove j from candidates[4][:3] and candidates[4][6:]
                    for counter in range(3):
                        if j in candidates[4][counter]:
                            candidates[4][counter].remove(j)
                        notCandidates[4][counter].append(j)
                    for counter in range(6,9):
                        if j in candidates[4][counter]:
                            candidates[4][counter].remove(j)
                        notCandidates[4][counter].append(j)
                elif boxNumber == 6:
                    #remove j from candidates[4][:6]
                    for counter in range(6):
                        if j in candidates[4][counter]:
                            candidates[4][counter].remove(j)
                        notCandidates[4][counter].append(j)
                elif boxNumber == 7:
                    #remove j from candidates[7][3:]
                    for counter in range(3,9):
                        if j in candidates[7][counter]:
                            candidates[7][counter].remove(j)
                        notCandidates[7][counter].append(j)
                elif boxNumber == 8:
                    #remove j from candidates[7][:3] and candidates[7][6:]
                    for counter in range(3):
                        if j in candidates[7][counter]:
                            candidates[7][counter].remove(j)
                        notCandidates[7][counter].append(j)
                    for counter in range(6,9):
                        if j in candidates[7][counter]:
                            candidates[7][counter].remove(j)
                        notCandidates[7][counter].append(j)
                elif boxNumber == 9:
                    #remove j from candidates[7][:6]
                    for counter in range(6):
                        if j in candidates[7][counter]:
                            candidates[7][counter].remove(j)
                        notCandidates[7][counter].append(j)
            elif j in r3 and j not in r1 and j not in r2:
                #remove from candidates and insert into not candidates
                if boxNumber == 1:
                    #remove j from candidates[2][3:]
                    for counter in range(3,9):
                        if j in candidates[2][counter]:
                            candidates[2][counter].remove(j)
                        notCandidates[2][counter].append(j)
                elif boxNumber == 2:
                    #remove j from candidates[2][0:3] and candidates[2][6:]
                    for counter in range(3):
                        if j in candidates[2][counter]:
                            candidates[2][counter].remove(j)
                        notCandidates[2][counter].append(j)
                    for counter in range(6,9):
                        if j in candidates[2][counter]:
                            candidates[2][counter].remove(j)
                        notCandidates[2][counter].append(j)
                elif boxNumber == 3:
                    #remove j from candidates[2][:6]
                    for counter in range(6):
                        if j in candidates[2][counter]:
                            candidates[2][counter].remove(j)
                        notCandidates[2][counter].append(j)
                elif boxNumber == 4:
                    #remove j from candidates[5][3:]
                    for counter in range(3,9):
                        if j in candidates[5][counter]:
                            candidates[5][counter].remove(j)
                        notCandidates[5][counter].append(j)
                elif boxNumber == 5:
                    #remove j from candidates[5][:3] and candidates[5][6:]
                    for counter in range(3):
                        if j in candidates[5][counter]:
                            candidates[5][counter].remove(j)
                        notCandidates[5][counter].append(j)
                    for counter in range(6,9):
                        if j in candidates[5][counter]:
                            candidates[5][counter].remove(j)
                        notCandidates[5][counter].append(j)
                elif boxNumber == 6:
                    #remove j from candidates[5][:6]
                    for counter in range(6):
                        if j in candidates[5][counter]:
                            candidates[5][counter].remove(j)
                        notCandidates[5][counter].append(j)
                elif boxNumber == 7:
                    #remove j from candidates[8][3:]
                    for counter in range(3,9):
                        if j in candidates[8][counter]:
                            candidates[8][counter].remove(j)
                        notCandidates[8][counter].append(j)
                elif boxNumber == 8:
                    #remove j from candidates[8][:3] and candidates[8][6:]
                    for counter in range(3):
                        if j in candidates[8][counter]:
                            candidates[8][counter].remove(j)
                        notCandidates[8][counter].append(j)
                    for counter in range(6,9):
                        if j in candidates[8][counter]:
                            candidates[8][counter].remove(j)
                        notCandidates[8][counter].append(j)
                elif boxNumber == 9:
                    #remove j from candidates[8][:6]
                    for counter in range(6):
                        if j in candidates[8][counter]:
                            candidates[8][counter].remove(j)
                        notCandidates[8][counter].append(j)

        boxNumber += 1
    zeroCounter = findCandidates()
#############################################################################
#pairsInRow
def pairsInRow(pair_rows):
    rowNumber = 1
    for i in pair_rows:
        #print(i,'\n')
        for j in range(8):
            for k in range(j+1,9):
                if len(i[0][j]) == 2 and i[0][j] == i[0][k]:
                    #Remove
                    for counter in range(9):
                        if counter != j and counter != k:
                            if i[0][j][0] in candidates[rowNumber - 1][counter]:
                                candidates[rowNumber - 1][counter].remove(i[0][j][0])
                                notCandidates[rowNumber - 1][counter].append(i[0][j][0])
                            if i[0][j][1] in candidates[rowNumber - 1][counter]:
                                candidates[rowNumber - 1][counter].remove(i[0][j][1])
                                notCandidates[rowNumber - 1][counter].append(i[0][j][1])

        rowNumber += 1
    zeroCounter = findCandidates()
#############################################################################
#pairsInColumn
def pairsInColumn(pair_columns):
    colNumber = 1
    for i in pair_columns:
        #print(i,'\n')
        for j in range(8):
            for k in range(j+1,9):
                if len(i[j]) == 2 and i[j] == i[k]:
                    #Remove
                    for counter in range(9):
                        if counter != j and counter != k:
                            if i[j][0] in candidates[counter][colNumber - 1]:
                                candidates[counter][colNumber - 1].remove(i[j][0])
                                notCandidates[counter][colNumber - 1].append(i[j][0])
                            if i[j][1] in candidates[counter][colNumber - 1]:
                                candidates[counter][colNumber - 1].remove(i[j][1])
                                notCandidates[counter][colNumber - 1].append(i[j][1])

        colNumber += 1
    zeroCounter = findCandidates()
#############################################################################
#pairsInBox
def pairsInBox(pair_boxes):
    boxNumber = 1
    for box in pair_boxes:
        #print(i,'\n')
        for rowA in range(3):
            for colA in range(3):
                if rowA == 2 and colA == 2:
                    break
                for rowB in range(rowA,3):
                    for colB in range(3):
                        if rowA == rowB and colA >= colB:
                            continue
                        if len(box[rowA][colA]) == 2 and box[rowA][colA] == box[rowB][colB]:
                            #Remove
                            if boxNumber == 1:
                                for row in range(3):
                                    for col in range(3):
                                        if row == rowA and col == colA:
                                            continue
                                        elif row == rowB and col == colB:
                                            continue
                                        else:
                                            if box[rowA][colA][0] in candidates[row][col]:
                                                candidates[row][col].remove(box[rowA][colA][0])
                                                notCandidates[row][col].append(box[rowA][colA][0])
                                            if box[rowA][colA][1] in candidates[row][col]:
                                                candidates[row][col].remove(box[rowA][colA][1])
                                                notCandidates[row][col].append(box[rowA][colA][1])

                            elif boxNumber == 2:
                                for row in range(3):
                                    for col in range(3):
                                        if row == rowA and col == colA:
                                            continue
                                        elif row == rowB and col == colB:
                                            continue
                                        else:
                                            if box[rowA][colA][0] in candidates[row][col+3]:
                                                candidates[row][col+3].remove(box[rowA][colA][0])
                                                notCandidates[row][col+3].append(box[rowA][colA][0])
                                            if box[rowA][colA][1] in candidates[row][col+3]:
                                                candidates[row][col+3].remove(box[rowA][colA][1])
                                                notCandidates[row][col+3].append(box[rowA][colA][1])

                            elif boxNumber == 3:
                                for row in range(3):
                                    for col in range(3):
                                        if row == rowA and col == colA:
                                            continue
                                        elif row == rowB and col == colB:
                                            continue
                                        else:
                                            if box[rowA][colA][0] in candidates[row][col+6]:
                                                candidates[row][col+6].remove(box[rowA][colA][0])
                                                notCandidates[row][col+6].append(box[rowA][colA][0])
                                            if box[rowA][colA][1] in candidates[row][col+6]:
                                                candidates[row][col+6].remove(box[rowA][colA][1])
                                                notCandidates[row][col+6].append(box[rowA][colA][1])
                            elif boxNumber == 4:
                                for row in range(3):
                                    for col in range(3):
                                        if row == rowA and col == colA:
                                            continue
                                        elif row == rowB and col == colB:
                                            continue
                                        else:
                                            if box[rowA][colA][0] in candidates[row+3][col]:
                                                candidates[row+3][col].remove(box[rowA][colA][0])
                                                notCandidates[row+3][col].append(box[rowA][colA][0])
                                            if box[rowA][colA][1] in candidates[row+3][col]:
                                                candidates[row+3][col].remove(box[rowA][colA][1])
                                                notCandidates[row+3][col].append(box[rowA][colA][1])

                            elif boxNumber == 5:
                                for row in range(3):
                                    for col in range(3):
                                        if row == rowA and col == colA:
                                            continue
                                        elif row == rowB and col == colB:
                                            continue
                                        else:
                                            if box[rowA][colA][0] in candidates[row+3][col+3]:
                                                candidates[row+3][col+3].remove(box[rowA][colA][0])
                                                notCandidates[row+3][col+3].append(box[rowA][colA][0])
                                            if box[rowA][colA][1] in candidates[row+3][col+3]:
                                                candidates[row+3][col+3].remove(box[rowA][colA][1])
                                                notCandidates[row+3][col+3].append(box[rowA][colA][1])

                            elif boxNumber == 6:
                                for row in range(3):
                                    for col in range(3):
                                        if row == rowA and col == colA:
                                            continue
                                        elif row == rowB and col == colB:
                                            continue
                                        else:
                                            if box[rowA][colA][0] in candidates[row+3][col+6]:
                                                candidates[row+3][col+6].remove(box[rowA][colA][0])
                                                notCandidates[row+3][col+6].append(box[rowA][colA][0])
                                            if box[rowA][colA][1] in candidates[row+1][col+6]:
                                                candidates[row+3][col+6].remove(box[rowA][colA][1])
                                                notCandidates[row+3][col+6].append(box[rowA][colA][1])

                            elif boxNumber == 7:
                                for row in range(3):
                                    for col in range(3):
                                        if row == rowA and col == colA:
                                            continue
                                        elif row == rowB and col == colB:
                                            continue
                                        else:
                                            if box[rowA][colA][0] in candidates[row+6][col]:
                                                candidates[row+6][col].remove(box[rowA][colA][0])
                                                notCandidates[row+6][col].append(box[rowA][colA][0])
                                            if box[rowA][colA][1] in candidates[row+6][col]:
                                                candidates[row+6][col].remove(box[rowA][colA][1])
                                                notCandidates[row+6][col].append(box[rowA][colA][1])

                            elif boxNumber == 8:
                                for row in range(3):
                                    for col in range(3):
                                        if row == rowA and col == colA:
                                            continue
                                        elif row == rowB and col == colB:
                                            continue
                                        else:
                                            if box[rowA][colA][0] in candidates[row+6][col+3]:
                                                candidates[row+6][col+3].remove(box[rowA][colA][0])
                                                notCandidates[row+6][col+3].append(box[rowA][colA][0])
                                            if box[rowA][colA][1] in candidates[row+6][col+3]:
                                                candidates[row+6][col+3].remove(box[rowA][colA][1])
                                                notCandidates[row+6][col+3].append(box[rowA][colA][1])

                            elif boxNumber == 9:
                                for row in range(3):
                                    for col in range(3):
                                        if row == rowA and col == colA:
                                            continue
                                        elif row == rowB and col == colB:
                                            continue
                                        else:
                                            if box[rowA][colA][0] in candidates[row+6][col+6]:
                                                candidates[row+6][col+6].remove(box[rowA][colA][0])
                                                notCandidates[row+6][col+6].append(box[rowA][colA][0])
                                            if box[rowA][colA][1] in candidates[row+6][col+6]:
                                                candidates[row+6][col+6].remove(box[rowA][colA][1])
                                                notCandidates[row+6][col+6].append(box[rowA][colA][1])

        boxNumber += 1
    zeroCounter = findCandidates()


#############################################################################
#processOfElimination
def processOfElimination():
    
    ################################
    # Boxes 1 # if only one in box #
    ################################

    b1 = [x[:3] for x in candidates[:3]]
    b2 = [x[3:6] for x in candidates[:3]]
    b3 = [x[6:] for x in candidates[:3]]
    b4 = [x[:3] for x in candidates[3:6]]
    b5 = [x[3:6] for x in candidates[3:6]]
    b6 = [x[6:] for x in candidates[3:6]]
    b7 = [x[:3] for x in candidates[6:]]
    b8 = [x[3:6] for x in candidates[6:]]
    b9 = [x[6:] for x in candidates[6:]]

    boxes = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    
    ifOnlyOneInBox(boxes)

    ##################################
    # Boxes 2 # candidateTrimmingRow #
    ##################################

    candidateTrimmingRow(boxes)
    
    ##################################
    # Boxes 3 # candidateTrimmingCol #
    ##################################
    
    candidateTrimmingCol(boxes)
    
    #############################
    # Rows # if only one in row #
    #############################
    r1 = [candidates[0]]
    r2 = [candidates[1]]
    r3 = [candidates[2]]
    r4 = [candidates[3]]
    r5 = [candidates[4]]
    r6 = [candidates[5]]
    r7 = [candidates[6]]
    r8 = [candidates[7]]
    r9 = [candidates[8]]
    
    rows = [r1,r2,r3,r4,r5,r6,r7,r8,r9]
    
    ifOnlyOneInRow(rows)

    ###################################
    # Columns # if only one in column #
    ###################################

    c1 = [x[0] for x in candidates[:]]
    c2 = [x[1] for x in candidates[:]]
    c3 = [x[2] for x in candidates[:]]
    c4 = [x[3] for x in candidates[:]]
    c5 = [x[4] for x in candidates[:]]
    c6 = [x[5] for x in candidates[:]]
    c7 = [x[6] for x in candidates[:]]
    c8 = [x[7] for x in candidates[:]]
    c9 = [x[8] for x in candidates[:]]

    columns = [c1,c2,c3,c4,c5,c6,c7,c8,c9]

    ifOnlyOneInColumn(columns)

    #Pairs

    findPairs()
    
    ##################
    # Pairs in boxes #
    ##################

    pb1 = [x[:3] for x in pairs[:3]]
    pb2 = [x[3:6] for x in pairs[:3]]
    pb3 = [x[6:] for x in pairs[:3]]
    pb4 = [x[:3] for x in pairs[3:6]]
    pb5 = [x[3:6] for x in pairs[3:6]]
    pb6 = [x[6:] for x in pairs[3:6]]
    pb7 = [x[:3] for x in pairs[6:]]
    pb8 = [x[3:6] for x in pairs[6:]]
    pb9 = [x[6:] for x in pairs[6:]]

    pair_boxes = [pb1,pb2,pb3,pb4,pb5,pb6,pb7,pb8,pb9]

    pairsInBox(pair_boxes)

    #################
    # Pairs in rows #
    #################

    pr1 = [pairs[0]]
    pr2 = [pairs[1]]
    pr3 = [pairs[2]]
    pr4 = [pairs[3]]
    pr5 = [pairs[4]]
    pr6 = [pairs[5]]
    pr7 = [pairs[6]]
    pr8 = [pairs[7]]
    pr9 = [pairs[8]]
    
    pair_rows = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8,pr9]

    pairsInRow(pair_rows)

    ####################
    # Pairs in columns #
    ####################

    pc1 = [x[0] for x in pairs[:]]
    pc2 = [x[1] for x in pairs[:]]
    pc3 = [x[2] for x in pairs[:]]
    pc4 = [x[3] for x in pairs[:]]
    pc5 = [x[4] for x in pairs[:]]
    pc6 = [x[5] for x in pairs[:]]
    pc7 = [x[6] for x in pairs[:]]
    pc8 = [x[7] for x in pairs[:]]
    pc9 = [x[8] for x in pairs[:]]

    pair_columns = [pc1,pc2,pc3,pc4,pc5,pc6,pc7,pc8,pc9]

    pairsInColumn(pair_columns)

#############################################
#testing
#findCandidates()
#printIt(puzzle)
#printIt(candidates)
#processOfElimination()

def main():
    zeroCounter = findCandidates()
    lastZeroCounter = 0

    for i in range(100):
        if zeroCounter == 0:
            print('Solved!!!')
            printIt(puzzle)
            break

        if lastZeroCounter == zeroCounter:
            processOfElimination()
            zeroCounter = findCandidates()
            solve()
            if lastZeroCounter == zeroCounter:
                print('I give up!!!')
                findCandidates()
                printIt(candidates)
                break

        lastZeroCounter = zeroCounter
        printIt(puzzle)
        print('There are',zeroCounter,'zeros')
        solve()
        zeroCounter = findCandidates()




main()





