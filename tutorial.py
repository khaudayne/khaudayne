# Hàm kiểm tra trạng thái kết thúc của bàn cờ
## turnXorO string chứa 'x' hoặc 'o' ( lượt tương ứng ), x, y là tọa độ của điểm vừa chọn
def checkEnd(turnXorO, x, y):
    # Kiểm tra điều kiện thắng của x
    if(turnXorO == 'x'):
        # Kiểm tra hàng chứa 5 ô x liên tiếp
        count = 1
        d = 1
        while y + d < coL and chessT[x][y + d] == 'x':
            count += 1
            if count == 5:
                return True
            d += 1
        d = 1
        while y - d > -1 and chessT[x][y - d] == 'x':
            count += 1
            if count == 5:
                return True
            d += 1

        # Kiểm tra cột chứa 5 ô x liên tiếp
        count = 1
        d = 1
        while x + d < roW and chessT[x + d][y] == 'x':
            count += 1
            if count == 5:
                return True
            d += 1
        d = 1
        while x - d > -1 and chessT[x - d][y] == 'x':
            count += 1
            if count == 5:
                return True
            d += 1

        # Kiểm tra đường chéo C1 chứa 5 ô x liên tiếp
        count = 1
        d = 1
        while x + d < roW and y + d < coL and chessT[x + d][y + d] == 'x':
            count += 1
            if count == 5:
                return True
            d += 1
        d = 1
        while x - d > -1 and y - d > -1 and chessT[x - d][y - d] == 'x':
            count += 1
            if count == 5:
                return True
            d += 1

        # Kiểm tra đường chéo C2 chứa 5 ô x liên tiếp
        count = 1
        d = 1
        while x + d < roW and y - d > -1 and chessT[x + d][y - d] == 'x':
            count += 1
            if count == 5:
                return True
            d += 1
        d = 1
        while x - d > -1 and y + d < coL and chessT[x - d][y + d] == 'x':
            count += 1
            if count == 5:
                return True
            d += 1

    # Kiểm tra điều kiện thắng của o
    else:
        # Kiểm tra hàng chứa 5 ô o liên tiếp
        count = 1
        d = 1
        while y + d < coL and chessT[x][y + d] == 'o':
            count += 1
            if count == 5:
                return True
            d += 1
        d = 1
        while y - d > -1 and chessT[x][y - d] == 'o':
            count += 1
            if count == 5:
                return True
            d += 1

        # Kiểm tra cột chứa 5 ô o liên tiếp
        count = 1
        d = 1
        while x + d < roW and chessT[x + d][y] == 'o':
            count += 1
            if count == 5:
                return True
            d += 1
        d = 1
        while x - d > -1 and chessT[x - d][y] == 'o':
            count += 1
            if count == 5:
                return True
            d += 1

        # Kiểm tra đường chéo C1 chứa 5 ô o liên tiếp
        count = 1
        d = 1
        while x + d < roW and y + d < coL and chessT[x + d][y + d] == 'o':
            count += 1
            if count == 5:
                return True
            d += 1
        d = 1
        while x - d > -1 and y - d > -1 and chessT[x - d][y - d] == 'o':
            count += 1
            if count == 5:
                return True
            d += 1

        # Kiểm tra đường chéo C2 chứa 5 ô o liên tiếp 
        count = 1
        d = 1
        while x + d < roW and y - d > -1 and chessT[x + d][y - d] == 'o':
            count += 1
            if count == 5:
                return True
            d += 1
        d = 1
        while x - d > -1 and y + d < coL and chessT[x - d][y + d] == 'o':
            count += 1
            if count == 5:
                return True
            d += 1

# Hàm tạo terminal game
def printT():
    print(' ', end = '')
    for i in range(coL):
        print(' ', i + 1, sep = '', end = '')
    print()
    for i in range(roW):
        print(i + 1, ' ',sep = '', end = '')
        for j in range(coL):
            print(chessT[i][j], ' ', sep = '', end = '')
        print()
    


   
# Tic tac toe roW = coL = 3, mở rộng XO sau
roW = int(input('Nhập chiều dài hàng: '))
coL = int(input('Nhập chiều dài cột: '))

while roW < 5 or coL < 5:
    print('Kích thước trò chơi quá bé! Vui lòng nhập lại.')
    roW = int(input('Nhập chiều dài hàng: '))
    coL = int(input('Nhập chiều dài cột: '))

# Tạo bàn cờ kích thước roW * coL
chessT = [[' ' for i in range(coL)] for i in range(roW)]

# Mảng kiểm tra xem vị trí trên bàn cờ đã được chọn hay chưa
checkChessT = [[False for i in range(coL)] for i in range(roW)]

# Đánh dấu số lượt chơi
numPlay = 0

printT()
checkE = False      # Giá trị kiểm tra kết thúc trò chơi hay chưa
turnXorO = 'x'      # Biến thể hiện lượt của x hoặc o
while not checkE:
    if(turnXorO == 'x'):
        print('Tới lượt x: ', end = '')
    else:
        print('Tới lượt o: ', end = '')
    [x, y] = [int(x) for x in input().split()]
    # Kiểm tra tọa độ hợp lệ hay không
    if 0 > x or 0 > y or x > roW or y > coL or checkChessT[x - 1][y - 1]:
        print('Tọa độ không hợp lệ, vui lòng nhập lại!')
        printT()
        continue
    if(turnXorO == 'x'):
        checkChessT[x - 1][y - 1] = True
        chessT[x - 1][y - 1] = turnXorO

        checkE = checkEnd(turnXorO, x - 1, y - 1)
        if checkE:
            printT()
            print('x giành chiến thắng!')
            break
        turnXorO = 'o'
    else:
        checkChessT[x - 1][y - 1] = True
        chessT[x - 1][y - 1] = turnXorO

        checkE = checkEnd(turnXorO, x - 1, y - 1)
        if checkE:
            printT()
            print('o giành chiến thắng!')
            break
        turnXorO = 'x'
    printT()
    numPlay += 1
    if numPlay == roW * coL:
        print('Hòa!')
        break
