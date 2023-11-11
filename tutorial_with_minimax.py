#TIC TAC TOE 3x3 với minmax
import random
import time
import math


#_______________________________________________________________________________________
#_________________________________________phần AI____________________________________
#đối với phiên bản 3x3 này ta mặc định với AI sẽ đi quân o và người chơi sẽ đi quân x
COMP='o'
HUMAN='x'
#hàm tính điểm cho trạng thái bàn cờ, được sử dụng khi 1 trong 2 chiến thắng hoặc hoà
#Điểm được tính: thắng +1, thua -1, hoà 0
#thắng
def evaluate(state):
    if checkWin(state, COMP):
        score = +1
    elif checkWin(state, HUMAN):
        score = -1
    else:
        score = 0
    return score

#hàm này sử dụng để tìm tất cả ô trống còn lại ở trạng thái hiện tại
#dùng cho duyệt qua các ô trống trong minimax

def emptyBox(state):
    boxs = []

    for x, row in enumerate(state):
        for y, box in enumerate(row):
            if box == ' ':
                boxs.append([x, y])
    return boxs

#chương trình nay coi máy là MAximizer và người chơi là Minimizer
#vì thế khởi tạo giá trị ban đầu cho MAximizer là -inf và Minimizer là +inf
#maximizer sẽ tìm giá trị lớn nhất trong các giá trị trả về của các nước đi
#Sử dụng thuật toán quay lui, duyệt theo chiều sâu

#alpha là giá trị lớn nhất tìm được trong các nước đi của Maximizer
#beta là giá trị nhỏ nhất tìm được trong các nước đi của Minimizer
#nếu alpha >= beta nghĩa là ở nhánh đó, Minimizer sẽ không chọn nước đi nào tốt hơn
#nên ta cắt tỉa nhánh đó
def minimax(state, depth, player, alpha, beta):
    if player == COMP:
        best = [-1, -1, -math.inf]
    else:
        best = [-1, -1, math.inf]

    if depth == 0 or gameOver(state):
        score = evaluate(state)
        return [-1, -1, score]

    for box in emptyBox(state):
        x, y = box[0], box[1]
        state[x][y] = player
        score = minimax(state, depth - 1, HUMAN if player == COMP else COMP, alpha, beta)
        state[x][y] = ' '
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score 
            alpha = max(alpha, best[2])
        else:
            if score[2] < best[2]:
                best = score 
            beta = min(beta, best[2])

        if beta <= alpha:
            break  # Cắt tỉa alpha-beta

    return best


#Hàm trả về nước đi tối ưu cho AI
#Sử dụng minimax(dòng 36) để tìm nước đi tối ưu
def AI_smartMove(state):
    #nếu bàn cờ trống(cả 9 ô trống) thì trả về vị trí ngẫu nhiên
    depth = len(emptyBox(state))
    if depth == 0 or gameOver(state):
        return -1, -1
    move = minimax(state, depth, COMP, -math.inf, math.inf)
    x, y = move[0], move[1]
    return x, y

#_______________________________________________________________________________________
#_________________________________________Xử lí logic___________________________________
# Hàm kiểm tra game có kết thúc hay chưa
def gameOver(state):
    return checkWin(state, HUMAN) or checkWin(state, COMP)
# Hàm kiểm tra điều kiện thắng dựa trên trạng thái bàn cờ và
def checkWin(state, turn):
    roW = len(state)
    coL = len(state[0])

    # Kiểm tra điều kiện thắng của x
    if turn == 'x':
        # Kiểm tra hàng chứa 3 ô x liên tiếp
        for x in range(roW):
            for i in range(coL):
                if state[x][i] != 'x':
                    break
                if i == coL - 1:
                    return True

        # Kiểm tra cột chứa 3 ô x liên tiếp
        for y in range(coL):
            for i in range(roW):
                if state[i][y] != 'x':
                    break
                if i == roW - 1:
                    return True
        # Kiểm tra đường chéo C1 chứa 3 ô x liên tiếp
        for i in range(roW):
            if state[i][i] != 'x':
                break
            if i == roW - 1:
                return True
            # Kiểm tra đường chéo C2 chứa 3 ô x liên tiếp
        for i in range(roW):
            if state[i][(roW - 1) - i] != 'x':
                break
            if i == roW - 1:
                return True
    else:
        # Kiểm tra điều kiện thắng của o
        # Kiểm tra hàng chứa 3 ô o liên tiếp
        for x in range(roW):
            for i in range(coL):
                if state[x][i] != 'o':
                    break
                if i == coL - 1:
                    return True

        # Kiểm tra cột chứa 3 ô o liên tiếp
        for y in range(coL):
            for i in range(roW):
                if state[i][y] != 'o':
                    break
                if i == roW - 1:
                    return True

        # Kiểm tra đường chéo C1 chứa 3 ô o liên tiếp
        for i in range(roW):
            if state[i][i] != 'o':
                break
            if i == roW - 1:
                return True

        # Kiểm tra đường chéo C2 chứa 3 ô o liên tiếp
        if x + y == roW - 1:
            for i in range(roW):
                if state[i][(roW - 1) - i] != 'o':
                    break
                if i == roW - 1:
                    return True

    return False

# Hàm tạo terminal game
def printT():
    print(' ', end = '')
    for i in range(coL):
        print(' ', i + 1, sep = '', end = '')
    print()
    for i in range(roW):
        print(i + 1, '|',sep = '', end = '')
        for j in range(coL):
            print(chessT[i][j], '|', sep = '', end = '')
        print()
    
#_______________________________________________________________________________________
#_________________________________________phần tương tác khởi tạo trò chơi_______________________
# Tic tac toe roW = coL = 3, mở rộng XO sau
roW = int(input('Nhập chiều dài hàng: '))
coL = int(input('Nhập chiều dài cột: '))
# Tạo bàn cờ kích thước roW * coL
chessT = [[' ' for i in range(coL)] for i in range(roW)]
# Mảng kiểm tra xem vị trí trên bàn cờ đã được chọn hay chưa
checkChessT = [[False for i in range(coL)] for i in range(roW)]

printT()
checkE = False
numPlay=0

turnXorO=random.choice(['x','o'])  
if turnXorO =='x':  
    print('x đánh trước')
else:
    print('o đánh trước')

while not checkE:
    if(turnXorO == 'x'):
        print('Tới lượt x: ', end = '')
        x, y = input().split()
        x = int(x)
        y = int(y)
    else:
        #AI sẽ đi quân o
        time.sleep(1)
        print('Tới lượt o: ', end = '')
        temp=AI_smartMove(chessT)
        x=temp[0]+1
        y=temp[1]+1
        print(x,y)
        print(end='\n')

    
    # Kiểm tra tọa độ hợp lệ hay không
    if 0 > x or 0 > y or x > roW or y > coL or checkChessT[x - 1][y - 1]:
        print('Tọa độ không hợp lệ, vui lòng nhập lại!')
        printT()
        continue
    if(turnXorO == 'x'):
        numPlay+=1
        checkChessT[x - 1][y - 1] = True
        chessT[x - 1][y - 1] = turnXorO
        checkE = checkWin(chessT,turnXorO)
        if checkE:
            printT()
            print('x giành chiến thắng!')
            break
        elif numPlay==9:
            printT()
            #hoà cờ, cay quá, phục thù không?
            print("Hòa! x")
            print('phục thù? (y/n)')
            if(input()=='y'):
                checkE=False
                chessT = [[' ' for i in range(coL)] for i in range(roW)]
                checkChessT = [[False for i in range(coL)] for i in range(roW)]
                numPlay=0
                printT()
                continue
            else:
                break
        turnXorO = 'o'
    else:
        numPlay+=1
        checkChessT[x - 1][y - 1] = True
        chessT[x - 1][y - 1] = turnXorO


        checkE = checkWin(chessT, turnXorO)
        if checkE:
            printT()
            print('o giành chiến thắng!')
            break
        elif numPlay==9:
            printT()
            #hoà cờ, cay quá, phục thù không?
            print("Hòa! o")
            print('phục thù? (y/n)')
            if(input()=='y'):
                checkE=False
                chessT = [[' ' for i in range(coL)] for i in range(roW)]
                checkChessT = [[False for i in range(coL)] for i in range(roW)]
                numPlay=0
                turnXorO = 'x'
                printT()
                continue
            else:
                break
        turnXorO = 'x'
    printT()
