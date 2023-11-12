# Import thư viện tạo giao diện đơn giản
import math
import random
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox 

# Hàm hover button
def on_enter(e):
    e.widget.config(bg='#99FFFF',fg = '#99FFFF')

#Hàm leave button
def on_leave(e):
    e.widget.config(bg='white', fg = 'white')

# Hàm heuristic h(n) đánh giá giá trị của bàn cờ:
def evaluate(state, player, x, y):
    if x != -1 and y != -1 and checkEnd(state, x, y)[0]:
        if player == HUMAN[0]:
            return math.inf
        else:
            return -math.inf
    
    numMark = 0
    if player == COMP[0]:
        while store_Human[numMark] != [-1, -1]:
            numMark += 1
        store_Human[numMark] = [x, y]
    else:
        while store_Comp[numMark] != [-1, -1]:
            numMark += 1
        store_Comp[numMark] = [x, y]

    total_Score_Comp = 0
    total_Score_Human = 0

    num4_Human = 0
    num4_Comp = 0

    num3_Human = 0
    num3_Comp = 0

    num3_Human_Block = 0
    num3_Comp_Block = 0

    num2_Human = 0
    num2_Comp = 0

    num2_Human_Block = 0
    num2_Comp_Block = 0

    near_By_Human = 0
    near_By_Comp = 0

    # Tính điểm cho Comp
    for xx, yy in store_Comp:
        if xx == -1 or yy == -1:
            break
        # Đếm theo hàng ngang
        a = False
        nSpace = 0
        if yy > 0 and chessT[xx][yy - 1] == HUMAN[0]:
            a = True
        for i in range(1, 5):
            if yy + i < colT[0] and chessT[xx][yy + i] == HUMAN[0]:
                if a:
                    break
                else:
                    if chessT[xx][yy + i - 1] != ' ':
                        if i - nSpace - 1 == 1:
                            num2_Comp_Block += 1
                        elif i - nSpace - 1 == 2:
                            num3_Comp_Block += 1
                        elif i - nSpace - 1 == 3:
                            num4_Comp += 1
                    else:
                        if i - nSpace - 1 == 1:
                            num2_Comp += 1
                        elif i - nSpace - 1 == 2:
                            num3_Comp += 1
                    break
            elif yy + i < colT[0] and chessT[xx][yy + i] == ' ':
                nSpace += 1
            if i == 4 and yy + i < colT[0]:
                if i - nSpace == 1:
                    if a:
                        num2_Comp_Block += 1
                    else:
                        num2_Comp += 1
                elif i - nSpace == 2:
                    if a:
                        num3_Comp_Block += 1
                    else:
                        num3_Comp += 1
                elif i - nSpace == 3:
                    num4_Comp += 1
            if yy + i >= colT[0]:
                if a:
                    break
                else:
                    if i - nSpace - 1 == 1:
                        num2_Comp += 1
                    elif i - nSpace - 1 == 2:
                        num3_Comp += 1
                    elif i - nSpace - 1== 3:
                        num4_Comp += 1
                    break


        # Đếm theo hàng dọc
        a = False
        nSpace = 0
        if xx > 0 and chessT[xx - 1][yy] == HUMAN[0]:
            a = True
        for i in range(1, 5):
            if xx + i < rowT[0] and chessT[xx + i][yy] == HUMAN[0]:
                if a:
                    break
                else:
                    if chessT[xx + i - 1][yy] != ' ':
                        if i - nSpace - 1 == 1:
                            num2_Comp_Block += 1
                        elif i - nSpace - 1 == 2:
                            num3_Comp_Block += 1
                        elif i - nSpace - 1 == 3:
                            num4_Comp += 1
                    else:
                        if i - nSpace - 1 == 1:
                            num2_Comp += 1
                        elif i - nSpace - 1 == 2:
                            num3_Comp += 1
                    break
            elif xx + i < colT[0] and chessT[xx + i][yy] == ' ':
                nSpace += 1
            if i == 4 and xx + i < rowT[0]:
                if i - nSpace == 1:
                    if a:
                        num2_Comp_Block += 1
                    else:
                        num2_Comp += 1
                elif i - nSpace == 2:
                    if a:
                        num3_Comp_Block += 1
                    else:
                        num3_Comp += 1
                elif i - nSpace == 3:
                    num4_Comp += 1
            if xx + i >= rowT[0]:
                if a:
                    break
                else:
                    if i - nSpace - 1 == 1:
                        num2_Comp += 1
                    elif i - nSpace -1 == 2:
                        num3_Comp += 1
                    elif i - nSpace -1 == 3:
                        num4_Comp += 1
                    break
        
        # Đếm theo đường chéo C1
        a = False
        nSpace = 0
        if yy > 0 and xx > 0 and chessT[xx - 1][yy - 1] == HUMAN[0]:
            a = True
        for i in range(1, 5):
            if yy + i < colT[0] and xx + i < rowT[0] and chessT[xx + i][yy + i] == HUMAN[0]:
                if a:
                    continue
                else:
                    if chessT[xx + i - 1][yy + i - 1] != ' ':
                        if i - nSpace - 1 == 1:
                            num2_Comp_Block += 1
                        elif i - nSpace - 1 == 2:
                            num3_Comp_Block += 1
                        elif i - nSpace - 1 == 3:
                            num4_Comp += 1
                    else:
                        if i - nSpace - 1 == 1:
                            num2_Comp += 1
                        elif i - nSpace - 1 == 2:
                            num3_Comp += 1
                    break
            elif yy + i < colT[0] and xx + i < rowT[0] and chessT[xx + i][yy + i] == ' ':
                nSpace += 1
            if i == 4 and yy + i < colT[0] and xx + i < rowT[0]:
                if i - nSpace == 1:
                    if a:
                        num2_Comp_Block += 1
                    else:
                        num2_Comp += 1
                elif i - nSpace == 2:
                    if a:
                        num3_Comp_Block += 1
                    else:
                        num3_Comp += 1
                elif i - nSpace == 3:
                    num4_Comp += 1
            if xx + i >= rowT[0] or yy + i >= colT[0]:
                if a:
                    break
                else:
                    if i - nSpace - 1 == 1:
                        num2_Comp += 1
                    elif i - nSpace - 1 == 2:
                        num3_Comp += 1
                    elif i - nSpace - 1 == 3:
                        num4_Comp += 1
                    break
        
        # Đếm theo đường chéo C2
        a = False
        nSpace = 0
        if yy < colT[0] - 1 and xx > 0 and chessT[xx - 1][yy + 1] == HUMAN[0]:
            a = True
        for i in range(1, 5):
            if yy - i >= 0 and xx + i < rowT[0] and chessT[xx + i][yy - i] == HUMAN[0]:
                if a:
                    continue
                else:
                    if chessT[xx + i - 1][yy - i + 1] != ' ':
                        if i - nSpace - 1 == 1:
                            num2_Comp_Block += 1
                        elif i - nSpace - 1 == 2:
                            num3_Comp_Block += 1
                        elif i - nSpace - 1 == 3:
                            num4_Comp += 1
                    else:
                        if i - nSpace - 1 == 1:
                            num2_Comp += 1
                        elif i - nSpace - 1 == 2:
                            num3_Comp += 1
                    break
            elif yy - i >= 0  and xx + i < rowT[0] and chessT[xx + i][yy - i] == ' ':
                nSpace += 1
            if i == 4 and yy - i >= 0  and xx + i < rowT[0]:
                if i - nSpace == 1:
                    if a:
                        num2_Comp_Block += 1
                    else:
                        num2_Comp += 1
                elif i - nSpace == 2:
                    if a:
                        num3_Comp_Block += 1
                    else:
                        num3_Comp += 1
                elif i - nSpace == 3:
                    num4_Comp += 1
            if xx + i >= rowT[0] or yy - i < 0:
                if a:
                    break
                else:
                    if i - nSpace - 1== 1:
                        num2_Comp += 1
                    elif i - nSpace - 1== 2:
                        num3_Comp += 1
                    elif i - nSpace - 1== 3:
                        num4_Comp += 1
                    break
        
        if xx + 1 < rowT[0] and chessT[xx + 1][yy] == HUMAN[0]:
            near_By_Comp += 1
        if yy + 1 < colT[0] and chessT[xx][yy + 1] == HUMAN[0]:
            near_By_Comp += 1
        if xx > 0 and chessT[xx - 1][yy] == HUMAN[0]:
            near_By_Comp += 1
        if yy > 0 and chessT[xx][yy - 1] == HUMAN[0]:
            near_By_Comp += 1
        if xx + 1 < rowT[0] and yy + 1 < colT[0] and chessT[xx + 1][yy + 1] == HUMAN[0]:
            near_By_Comp += 1
        if xx + 1 < rowT[0] and y > 0 and chessT[xx + 1][yy - 1] == HUMAN[0]:
            near_By_Comp += 1
        if yy + 1 < colT[0] and x > 0 and chessT[xx - 1][yy + 1] == HUMAN[0]:
            near_By_Comp += 1
        if yy > 0 and xx > 0 and chessT[xx - 1][yy - 1] == HUMAN[0]:
            near_By_Comp += 1

    # Tính điểm cho Người
    for xx, yy in store_Human:
        if xx == -1 or yy == -1:
            break
        # Đếm theo hàng ngang
        a = False
        nSpace = 0
        if yy > 0 and chessT[xx][yy - 1] == COMP[0]:
            a = True
        for i in range(1, 5):
            if yy + i < colT[0] and chessT[xx][yy + i] == COMP[0]:
                if a:
                    break
                else:
                    if chessT[xx][yy + i - 1] != ' ':
                        if i - nSpace - 1 == 1:
                            num2_Human_Block += 1
                        elif i - nSpace - 1 == 2:
                            num3_Human_Block += 1
                        elif i - nSpace - 1 == 3:
                            num4_Human += 1
                    else:
                        if i - nSpace - 1 == 1:
                            num2_Human += 1
                        elif i - nSpace - 1 == 2:
                            num3_Human += 1
                    break
            elif yy + i < colT[0] and chessT[xx][yy + i] == ' ':
                nSpace += 1
            if i == 4 and yy + i < colT[0]:
                if i - nSpace == 1:
                    if a:
                        num2_Human_Block += 1
                    else:
                        num2_Human += 1
                elif i - nSpace == 2:
                    if a:
                        num3_Human_Block += 1
                    else:
                        num3_Human += 1
                elif i - nSpace == 3:
                    num4_Human += 1
            if yy + i >= colT[0]:
                if a:
                    break
                else:
                    if i - nSpace - 1 == 1:
                        num2_Human += 1
                    elif i - nSpace - 1 == 2:
                        num3_Human += 1
                    elif i - nSpace - 1 == 3:
                        num4_Human += 1
                    break


        # Đếm theo hàng dọc
        a = False
        nSpace = 0
        if xx > 0 and chessT[xx - 1][yy] == COMP[0]:
            a = True
        for i in range(1, 5):
            if xx + i < rowT[0] and chessT[xx + i][yy] == COMP[0]:
                if a:
                    break
                else:
                    if chessT[xx + i - 1][yy] != ' ':
                        if i - nSpace - 1 == 1:
                            num2_Human_Block += 1
                        elif i - nSpace - 1 == 2:
                            num3_Human_Block += 1
                        elif i - nSpace - 1 == 3:
                            num4_Human += 1
                    else:
                        if i - nSpace - 1 == 1:
                            num2_Human += 1
                        elif i - nSpace - 1 == 2:
                            num3_Human += 1
                    break
            elif xx + i < colT[0] and chessT[xx + i][yy] == ' ':
                nSpace += 1
            if i == 4 and xx + i < rowT[0]:
                if i - nSpace == 1:
                    if a:
                        num2_Human_Block += 1
                    else:
                        num2_Human += 1
                elif i - nSpace == 2:
                    if a:
                        num3_Human_Block += 1
                    else:
                        num3_Human += 1
                elif i - nSpace == 3:
                    num4_Human += 1
            if xx + i >= rowT[0]:
                if a:
                    break
                else:
                    if i - nSpace - 1 == 1:
                        num2_Human += 1
                    elif i - nSpace - 1 == 2:
                        num3_Human += 1
                    elif i - nSpace - 1 == 3:
                        num4_Human += 1
                    break
        
        # Đếm theo đường chéo C1
        a = False
        nSpace = 0
        if yy > 0 and xx > 0 and chessT[xx - 1][yy - 1] == COMP[0]:
            a = True
        for i in range(1, 5):
            if yy + i < colT[0] and xx + i < rowT[0] and chessT[xx + i][yy + i] == COMP[0]:
                if a:
                    continue
                else:
                    if chessT[xx + i - 1][yy + i - 1] != ' ':
                        if i - nSpace - 1 == 1:
                            num2_Human_Block += 1
                        elif i - nSpace - 1 == 2:
                            num3_Human_Block += 1
                        elif i - nSpace - 1 == 3:
                            num4_Human += 1
                    else:
                        if i - nSpace - 1 == 1:
                            num2_Human += 1
                        elif i - nSpace - 1 == 2:
                            num3_Human += 1
                    break
            elif yy + i < colT[0] and xx + i < rowT[0] and chessT[xx + i][yy + i] == ' ':
                nSpace += 1
            if i == 4 and yy + i < colT[0] and xx + i < rowT[0]:
                if i - nSpace == 1:
                    if a:
                        num2_Human_Block += 1
                    else:
                        num2_Human += 1
                elif i - nSpace == 2:
                    if a:
                        num3_Human_Block += 1
                    else:
                        num3_Human += 1
                elif i - nSpace == 3:
                    num4_Human += 1
            if xx + i >= rowT[0] or yy + i >= colT[0]:
                if a:
                    break
                else:
                    if i - nSpace - 1 == 1:
                        num2_Human += 1
                    elif i - nSpace - 1 == 2:
                        num3_Human += 1
                    elif i - nSpace - 1 == 3:
                        num4_Human += 1
                    break
        
        # Đếm theo đường chéo C2
        a = False
        nSpace = 0
        if yy < colT[0] - 1 and xx > 0 and chessT[xx - 1][yy + 1] == COMP[0]:
            a = True
        for i in range(1, 5):
            if yy - i >= 0 and xx + i < rowT[0] and chessT[xx + i][yy - i] == COMP[0]:
                if a:
                    continue
                else:
                    if chessT[xx + i - 1][yy - i + 1] != ' ':
                        if i - nSpace - 1 == 1:
                            num2_Human_Block += 1
                        elif i - nSpace - 1 == 2:
                            num3_Human_Block += 1
                        elif i - nSpace - 1 == 3:
                            num4_Human += 1
                    else:
                        if i - nSpace - 1 == 1:
                            num2_Human += 1
                        elif i - nSpace - 1 == 2:
                            num3_Human += 1
                    break
            elif yy - i >= 0  and xx + i < rowT[0] and chessT[xx + i][yy - i] == ' ':
                nSpace += 1
            if i == 4 and yy - i >= 0 and xx + i < rowT[0]:
                if i - nSpace == 1:
                    if a:
                        num2_Human_Block += 1
                    else:
                        num2_Human += 1
                elif i - nSpace == 2:
                    if a:
                        num3_Human_Block += 1
                    else:
                        num3_Human += 1
                elif i - nSpace == 3:
                    num4_Human += 1
            if xx + i >= rowT[0] or yy - i < 0:
                if a:
                    break
                else:
                    if i - nSpace - 1 == 1:
                        num2_Human += 1
                    elif i - nSpace - 1 == 2:
                        num3_Human += 1
                    elif i - nSpace - 1 == 3:
                        num4_Human += 1
                    break
        
        if xx + 1 < rowT[0] and chessT[xx + 1][yy] == COMP[0]:
            near_By_Human += 1
        if yy + 1 < colT[0] and chessT[xx][yy + 1] == COMP[0]:
            near_By_Human += 1
        if xx > 0 and chessT[xx - 1][yy] == COMP[0]:
            near_By_Human += 1
        if yy > 0 and chessT[xx][yy - 1] == COMP[0]:
            near_By_Human += 1
        if xx + 1 < rowT[0] and yy + 1 < colT[0] and chessT[xx + 1][yy + 1] == COMP[0]:
            near_By_Human += 1
        if xx + 1 < rowT[0] and y > 0 and chessT[xx + 1][yy - 1] == COMP[0]:
            near_By_Human += 1
        if yy + 1 < colT[0] and x > 0 and chessT[xx - 1][yy + 1] == COMP[0]:
            near_By_Human += 1
        if yy > 0 and xx > 0 and chessT[xx - 1][yy - 1] == COMP[0]:
            near_By_Human += 1
    
    if player == HUMAN[0]:
        store_Comp[numMark] = [-1, -1]
        total_Score_Comp = 2 * near_By_Comp + 20 * num2_Comp_Block + 250 * num2_Comp + 1000 * num3_Comp_Block + 10000 * num3_Comp + 700000 * num4_Comp
        total_Score_Human = near_By_Human + 70 * num2_Human_Block + 100 * num2_Human + 4000 * num3_Human_Block + 100000 * num3_Human + 500000000 * num4_Human
        return total_Score_Comp - total_Score_Human
    else:
        store_Human[numMark] = [-1, -1]
        total_Score_Comp = near_By_Comp + 20 * num2_Comp_Block + 250 * num2_Comp + 4000 * num3_Comp_Block + 100000 * num3_Comp + 500000000 * num4_Comp
        total_Score_Human = 2 * near_By_Human + 70 * num2_Human_Block + 100 * num2_Human + 1000 * num3_Human_Block + 10000 * num3_Human + 700000 * num4_Human
        return total_Score_Comp - total_Score_Human
       
## turnXorO string chứa 'x' hoặc 'o' ( lượt tương ứng ), x, y là tọa độ của điểm vừa chọn
### Trả về 4 giá trị lần lượt là: 
    # - True / False : Kết thúc trò chơi hay không
    # - ['row', 'col', 'c1', 'c2']: Hướng của 5 x hoặc o liên tiếp. Tương đương 4 hướng [ -- , | , \ , /]
    # - d: Số phần tử đằng sau tọa độ vừa được chọn ( trong 5 x hoặc o liên tiếp )
    # - d1: Số phần tử đằng trước tọa độ vừa được chọn ( trong 5 x hoặc o liên tiếp )
    ## 3 giá trị cuối trả về nhằm mục tiêu bôi đỏ 5 x hoặc o liên tiếp
def checkEnd(turnXorO, x, y):
    roW = rowT[0]
    coL = colT[0]
    # Kiểm tra điều kiện thắng của x
    if(turnXorO == 'x'):
        # Kiểm tra hàng chứa 5 ô x liên tiếp
        count = 1
        d = 1
        while y + d < coL and chessT[x][y + d] == 'x':
            if count + d == 5:
                return True, 'row', 4, 0
            d += 1
        d -= 1
        d1 = 1
        while y - d1 > -1 and chessT[x][y - d1] == 'x':
            if count + d + d1 == 5:
                return True, 'row', d, d1
            d1 += 1

        # Kiểm tra cột chứa 5 ô x liên tiếp
        count = 1
        d = 1
        while x + d < roW and chessT[x + d][y] == 'x':
            if count + d== 5:
                return True, 'col', 4, 0
            d += 1
        d -= 1
        d1 = 1
        while x - d1 > -1 and chessT[x - d1][y] == 'x':
            if count + d + d1 == 5:
                return True, 'col', d, d1
            d1 += 1

        # Kiểm tra đường chéo C1 chứa 5 ô x liên tiếp
        count = 1
        d = 1
        while x + d < roW and y + d < coL and chessT[x + d][y + d] == 'x':
            if count + d == 5:
                return True, 'c1', 4, 0
            d += 1
        d -= 1
        d1 = 1
        while x - d1 > -1 and y - d1 > -1 and chessT[x - d1][y - d1] == 'x':
            if count + d + d1 == 5:
                return True, 'c1', d, d1
            d1 += 1

        # Kiểm tra đường chéo C2 chứa 5 ô x liên tiếp
        count = 1
        d = 1
        while x + d < roW and y - d > -1 and chessT[x + d][y - d] == 'x':
            if count + d == 5:
                return True, 'c2', 4, 0
            d += 1
        d -= 1
        d1 = 1
        while x - d1 > -1 and y + d1 < coL and chessT[x - d1][y + d1] == 'x':
            if count + d + d1 == 5:
                return True, 'c2', d, d1
            d1 += 1

    # Kiểm tra điều kiện thắng của o
    else:
        # Kiểm tra hàng chứa 5 ô o liên tiếp
        count = 1
        d = 1
        while y + d < coL and chessT[x][y + d] == 'o':
            if count + d == 5:
                return True, 'row', 4, 0
            d += 1
        d -= 1
        d1 = 1
        while y - d1 > -1 and chessT[x][y - d1] == 'o':
            if count + d + d1 == 5:
                return True, 'row', d, d1
            d1 += 1

        # Kiểm tra cột chứa 5 ô o liên tiếp
        count = 1
        d = 1
        while x + d < roW and chessT[x + d][y] == 'o':
            if count + d == 5:
                return True, 'col', 4, 0
            d += 1
        d -= 1
        d1 = 1
        while x - d1 > -1 and chessT[x - d1][y] == 'o':
            if count + d + d1 == 5:
                return True, 'col', d, d1
            d1 += 1

        # Kiểm tra đường chéo C1 chứa 5 ô o liên tiếp
        count = 1
        d = 1
        while x + d < roW and y + d < coL and chessT[x + d][y + d] == 'o':
            if count + d == 5:
                return True, 'c1', 4, 0
            d += 1
        d -= 1
        d1 = 1
        while x - d1 > -1 and y - d1 > -1 and chessT[x - d1][y - d1] == 'o':
            if count + d + d1 == 5:
                return True, 'c1', d, d1
            d1 += 1

        # Kiểm tra đường chéo C2 chứa 5 ô o liên tiếp 
        count = 1
        d = 1
        while x + d < roW and y - d > -1 and chessT[x + d][y - d] == 'o':
            if count + d == 5:
                return True, 'c2', 4, 0
            d += 1
        d -= 1
        d1 = 1
        while x - d1 > -1 and y + d1 < coL and chessT[x - d1][y + d1] == 'o':
            if count + d + d1 == 5:
                return True, 'c2', d, d1
            d1 += 1

    return False, None, None, None

# Hàm kiểm tra game kết thúc hay chưa
def gameOver(state, x, y):
    if x == -1 or y == -1:
        return False
    return checkEnd(state, x, y)[0]
# Hàm lấy tọa độ một điểm chưa được chọn ngẫu nhiên
def get_Point():
    while True:
        x = random.randint(rowT[0] // 2 - 1, rowT[0] // 2)
        y = random.randint(colT[0] // 2 -1, colT[0] // 2)
        return x, y

# Hàm minimax với thuật toán cắt tỉa alpha - beta
## Thêm paremeter x, y là tọa độ nước đi vừa đi
def minimax(state, depth, player, alpha, beta, x, y):
    if player == COMP[0]:
        best = [-1 , -1, -math.inf]
    else:
        best = [-1, -1, math.inf]
    
    if depth == 0 or gameOver(state, x, y):
        sc = evaluate(state, player, x, y)
        return [-1, -1, sc]
    
    for box in emptyBox(state):
        xx, yy = box[0], box[1]
        # Bỏ qua nếu tọa độ đưa vào đủ " tệ "
        numMark = 0
        while True:
            # 1
            if xx + 1 < rowT[0] and chessT[xx + 1][yy] != ' ':
                numMark += 1
                break
            # 2
            if yy + 1 < colT[0] and chessT[xx][yy + 1] != ' ':
                numMark += 1
                break
            # 3
            if xx > 0 and chessT[xx - 1][yy] != ' ':
                numMark += 1
                break
            # 4
            if yy > 0 and chessT[xx][yy - 1] != ' ':
                numMark += 1
                break
            # 5
            if xx + 1 < rowT[0] and yy + 1 < colT[0] and chessT[xx + 1][yy + 1] != ' ':
                numMark += 1
                break
            # 6
            if xx + 1 < rowT[0] and y > 0 and chessT[xx + 1][yy - 1] != ' ':
                numMark += 1
                break
            # 7
            if yy + 1 < colT[0] and x > 0 and chessT[xx - 1][yy + 1] != ' ':
                numMark += 1
                break
            # 8
            if yy > 0 and xx > 0 and chessT[xx - 1][yy - 1] != ' ':
                numMark += 1
                break
            # 9
            if yy - 2 >= 0 and xx - 2 >= 0 and chessT[xx - 2][yy - 2] != ' ':
                numMark += 1
                break
            # 10
            if yy - 1 >= 0 and xx - 2 >= 0 and chessT[xx - 2][yy - 1] != ' ':
                numMark += 1
                break
            # 11
            if yy >= 0 and xx - 2 >= 0 and chessT[xx - 2][yy] != ' ':
                numMark += 1
                break
            # 12
            if yy + 1 < colT[0] and xx  - 2 >= 0 and chessT[xx - 2][yy + 1] != ' ':
                numMark += 1
                break
            # 13
            if yy + 2 < colT[0] and xx  - 2 >= 0 and chessT[xx - 2][yy + 2] != ' ':
                numMark += 1
                break
            # 14
            if yy + 2 < colT[0] and xx - 1 >= 0 and chessT[xx - 1][yy + 2] != ' ':
                numMark += 1
                break
            # 15
            if yy + 2 < colT[0] and xx >= 0 and chessT[xx][yy + 2] != ' ':
                numMark += 1
                break
            # 16
            if yy + 2 < colT[0] and xx + 1 < rowT[0] and chessT[xx + 1][yy + 2] != ' ':
                numMark += 1
                break
            # 17
            if yy + 2 < colT[0] and xx + 2 < rowT[0] and chessT[xx + 2][yy + 2] != ' ':
                numMark += 1
                break
            # 18
            if yy + 1 < colT[0] and xx + 2 < rowT[0] and chessT[xx + 2][yy + 1] != ' ':
                numMark += 1
                break
            # 19
            if yy >= 0 and xx + 2 < rowT[0] and chessT[xx + 2][yy] != ' ':
                numMark += 1
                break
            # 20
            if yy - 1 >= 0 and xx + 2 < rowT[0] and chessT[xx + 2][yy - 1] != ' ':
                numMark += 1
                break
            # 21
            if yy - 2 >= 0 and xx + 2 < rowT[0] and chessT[xx + 2][yy - 2] != ' ':
                numMark += 1
                break
            #  22
            if yy - 2 >= 0 and xx + 1 < rowT[0] and chessT[xx + 1][yy - 2] != ' ':
                numMark += 1
                break
            # 23
            if yy - 2 >= 0 and xx >= 0 and chessT[xx][yy - 2] != ' ':
                numMark += 1
                break
            # 24
            if yy - 2 >= 0 and xx - 1 >= 0 and chessT[xx - 1][yy - 2] != ' ':
                numMark += 1
                break
            if numMark == 0:
                break

        if numMark == 0:
            continue

        state[xx][yy] = player
        score = minimax(state, depth - 1, HUMAN[0] if player == COMP[0] else COMP[0], alpha, beta, xx, yy)
        state[xx][yy] = ' '
        score[0], score[1] = xx, yy

        if player == COMP[0]:
            if score[2] > best[2]:
                best = score
            alpha = max(alpha, best[2])
        else:
            if score[2] < best[2]:
                best = score
            beta = min(beta, best[2])

        if beta <= alpha:
            break  # Cắt tỉa alpha - beta

    return best

# Hàm trả về nước đi tối ưu cho AI
def AI_smartMove(state):
    move = minimax(state, depth[0], COMP[0], -math.inf, math.inf, -1, -1)
    x, y = move[0], move[1]
    return x, y

# Hàm lấy hết ô trống còn lại trên bàn cờ
def emptyBox(state):
    boxs = []
    for i in range(rowT[0]):
        for j in range(colT[0]):
            if state[i][j] == ' ':
                boxs.append([i, j])
    return boxs

# Hàm xuất hiện chọn đánh X hay O khi chơi với máy
def choose_Type(e):
    typeGame = e.widget.get()
    try:
        if typeGame == 'Chơi với máy':
            clone_Label.grid_forget()
            clone_Label1.grid_forget()
            cbb_X_O.grid(row = 0, column = 3 , padx = 30)
            clone_Label_Depth.grid(row = 0, column = 1, padx = 2)
            cbb_Depth.grid(row = 0, column = 2)

        else:
            cbb_X_O.grid_forget()
            clone_Label_Depth.grid_forget()
            cbb_Depth.grid_forget()
            clone_Label.grid(row = 0, column = 2)
            clone_Label1.grid(row = 0, column = 1, padx = 117)
    except:
        pass

# Hàm xử lý độ khó trò chơi
def choose_Level(e):
    level_Game = e.widget.get()
    if level_Game == 'Cực dễ':
        depth[0] = 1
    elif level_Game == 'Dễ':
        depth[0] = 2
    elif level_Game == 'Trung bình':
        depth[0] = 3
    else:
        depth[0] = 4



# Hàm khi nhấn vào button giao diện trò chơi
def clicked(btn, x, y):
    if x == -1 or y == -1:
        return
    if checkChessT[x][y]:
        return
    checkChessT[x][y] = True
    numPlay[0] += 1
    if numPlay[0] % 2 == 0:
        if typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh O':
            store_Comp[numPlay[0]//2] = [x, y]
        if typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh X':
            store_Human[numPlay[0]//2] = [x, y]

        btn.unbind("<Leave>")
        btn.unbind("<Enter>")
        chessT[x][y] = 'x'
        btn.config(text = 'X',font=('Arial',15), bg = 'white', fg = 'black')

        # Kiểm tra điều kiện thắng của X
        checkE, typeWin, sT, eN = checkEnd('x', x, y)
        if checkE:
            sT = int(sT)
            eN = int(eN)

            if typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh O':
                turnWho.config(text='Máy giành chiến thắng!')
            elif typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh X':
                turnWho.config(text='Người giành chiến thắng!')
            else:
                turnWho.config(text='X giành chiến thắng!')

            play.config(text = 'Chơi lại')
            buttons = fr.winfo_children()

            # Tô màu 5 phần tử x liên tục
            buttons[x * colT[0] + y].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
            if typeWin == 'row':
                for i in range(sT):
                    buttons[x * colT[0] + y + i + 1].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
                for i in range(eN):
                    buttons[x * colT[0] + y - i - 1].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
            elif typeWin == 'col':
                for i in range(sT):
                    buttons[(x + i + 1) * colT[0] + y].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
                for i in range(eN):
                    buttons[(x - i - 1) * colT[0] + y].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
            elif typeWin == 'c1':
                for i in range(sT):
                    buttons[(x + i + 1) * colT[0] + y + i + 1].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
                for i in range(eN):
                    buttons[(x - i - 1) * colT[0] + y - i - 1].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
            else:
                for i in range(sT):
                    buttons[(x + i + 1) * colT[0] + y - i - 1].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
                for i in range(eN):
                    buttons[(x - i - 1) * colT[0] + y + i + 1].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')

            # Vô hiệu hóa các nút còn lại khi kết thúc trò chơi
            for i in range(rowT[0]):
                for j in range(colT[0]):
                    checkChessT[i][j] = True
            for btnChild in buttons:
                try:
                    btnChild.unbind("<Leave>")
                    btnChild.unbind("<Enter>")
                except:
                    pass
            return

        # Nếu bàn cờ hết chỗ đánh thì thông báo hòa
        if numPlay[0] == maxNumPlay[0]:
            turnWho.config(text='Hòa!')
            return
        
        if typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh O':
            turnWho.config(text = 'Tới lượt của bạn', font=('Arial, 15'))

        elif typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh X':
            turnWho.config(text = 'Tới lượt của máy', font=('Arial, 15'))
            x, y = AI_smartMove(chessT)
            buttons = fr.winfo_children()
            btn = buttons[x * colT[0] + y]
            clicked(btn, x, y)
        else:
            turnWho.config(text = 'Tới lượt của o', font=('Arial, 15'))

        
    else:
        if typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh X':
            store_Comp[numPlay[0]//2] = [x, y]
        if typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh O':
            store_Human[numPlay[0]//2] = [x, y]

        btn.unbind("<Leave>")
        btn.unbind("<Enter>")
        chessT[x][y] = 'o'
        btn.config(text = 'O',font=('Arial',15), bg = 'white', fg = 'black')

        # Kiểm tra điều kiện thắng của O
        checkE, typeWin, sT, eN = checkEnd('o', x, y)
        if checkE:
            sT = int(sT)
            eN = int(eN)
            
            if typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh O':
                turnWho.config(text='Người giành chiến thắng!')
            elif typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh X':
                turnWho.config(text='Máy giành chiến thắng!')
            else:
                turnWho.config(text='O giành chiến thắng!')

            play.config(text = 'Chơi lại')
            buttons = fr.winfo_children()

            # Tô màu 5 phần tử o liên tục
            buttons[x * colT[0] + y].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
            if typeWin == 'row':               
                for i in range(sT):
                    buttons[x * colT[0] + y + i + 1].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
                for i in range(eN):
                    buttons[x * colT[0] + y - i - 1].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
            elif typeWin == 'col':
                for i in range(sT):
                    buttons[(x + i + 1) * colT[0] + y].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
                for i in range(eN):
                    buttons[(x - i - 1) * colT[0] + y].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
            elif typeWin == 'c1':
                for i in range(sT):
                    buttons[(x + i + 1) * colT[0] + y + i + 1].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
                for i in range(eN):
                    buttons[(x - i - 1) * colT[0] + y - i - 1].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
            else:
                for i in range(sT):
                    buttons[(x + i + 1) * colT[0] + y - i - 1].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')
                for i in range(eN):
                    buttons[(x - i - 1) * colT[0] + y + i + 1].config(fg = 'white', bg = 'red', activebackground = 'red', activeforeground = 'white')

            # Vô hiệu hóa các button còn lại khi kết thúc trò chơi
            for i in range(rowT[0]):
                for j in range(colT[0]):
                    checkChessT[i][j] = True
            for btnChild in buttons:
                try:
                    btnChild.unbind("<Leave>")
                    btnChild.unbind("<Enter>")
                except:
                    pass
            return
            
        if numPlay[0] == maxNumPlay[0]:
            turnWho.config(text='Hòa!')
            return
        if typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh O':
            turnWho.config(text = 'Tới lượt của máy', font=('Arial, 15'))
            x, y = AI_smartMove(chessT)
            buttons = fr.winfo_children()
            btn = buttons[x * colT[0] + y]
            clicked(btn, x, y)
        elif typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh X':
            turnWho.config(text = 'Tới lượt của bạn', font=('Arial, 15'))
        else:
            turnWho.config(text = 'Tới lượt của x', font=('Arial, 15'))
    


    
# Hàm xóa hết giao diện bàn cờ khi ấn núi chơi 
def desChild():
    for widget in fr.winfo_children():
        widget.destroy()

# Hàm khi bấm núi chơi  
def btnPlay():
    turnWho.focus()
    # roW và coL lần lượt là hàng và cột của bàn cờ
    try:
        roW = int(e1.get())
        coL = int(e2.get())
    except:
        messagebox.showwarning('Show Warning', 'Vui lòng nhập đúng giá trị hàng và cột!')
        return
        
    if roW < 5 or coL < 5:
        messagebox.showwarning('Show Warning', 'Kích thước bảng quá bé, vui lòng nhập lại!')
        return
    
    if roW > 20 or coL > 40:
        messagebox.showwarning('Show Warning', 'Kích thước bảng quá to, vui lòng nhập lại!')
        return
    desChild()
    typeG[0] = cbb_Type_Play.get()
    if typeG[0] == 'Chơi với máy':
        choose_X_O[0] = cbb_X_O.get()
    # Khởi tạo bàn cờ và số lượt đầu trận
    numPlay[0] = -1
    rowT[0] = roW
    colT[0] = coL
    maxNumPlay[0] = roW * coL - 1
    play.config(text = 'Làm mới bàn cờ')
    for i in range(roW):
        for j in range(coL):
            chessT[i][j] = ' '
            checkChessT[i][j] = False
    for i in range(roW * coL):
        store_Human[i] = [-1, -1]
        store_Comp[i] = [-1, -1]
    turnWho.config(text = 'Tới lượt của x', font=('Arial, 15'))
    if typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh X':
        turnWho.config(text = 'Tới lượt của bạn')
    # Xây dựng giao diện trò chơi bằng mảng 2 chiều gồm roW * coL Button 
    buttons = [[Button(fr,font=('Arial', 15), width=5, height=2) for i in range(coL)] for i in range(roW)]
    for b in range(roW):
        for a in range(coL):
            buttons[b][a].config(bg = 'white', activebackground = 'white',width = 3, height = 1)
            buttons[b][a].bind("<Enter>", on_enter)
            buttons[b][a].bind("<Leave>", on_leave)
            buttons[b][a].config(command= lambda btn =  buttons[b][a], x = b, y = a: clicked(btn, x, y))
            buttons[b][a].grid( row = b, column = a)
    # Nếu chơi với máy lấy tọa độ ngẫu nhiên rồi đánh vào bàn cờ
    if typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh O':
        COMP[0] = 'x'
        HUMAN[0] = 'o'
        x, y = get_Point()
        buttons = fr.winfo_children()
        btn = buttons[x * colT[0] + y]
        clicked(btn, x, y)

# Bàn cờ mặc định chessT
chessT = [[' ' for i in range(100)] for i in range(100)]
# Đánh dấu các điểm đã chọn
checkChessT = [[False for i in range(100)] for i in range(100)]
# Số lượt đã chơi trong ván hiện tại
numPlay = [-1]
# Số lượt đi tối đa
maxNumPlay = [0]
# Giá trị số hàng và cột của bàn cờ
rowT = [0]
colT = [0]
# Thể loại chơi
typeG = [0]
# Đánh X hay O
choose_X_O = [0]
# Độ sâu của trò chơi
depth = [1]
# Chữ cái của Computer và Human
COMP = ['o']
HUMAN = ['x']
# Biến lưu trữ vị trí đã đi qua của người và máy
store_Comp = [[-1, -1] for i in range(1000)]
store_Human = [[-1, -1] for i in range(1000)]

### Xây dựng giao diện game 
# Widget root cho giao diện
parent = Tk()
parent.title('Caro')

# Frame chứa Entry lấy giá trị của hàng
frHang = Frame(parent)
frHang.pack()
nRow = Label(frHang, text = "Nhập số hàng:",width=15).grid(row = 0, column = 0)
e1 = Entry(frHang)
e1.insert(END, '10')
e1.focus()
e1.grid(row = 0, column = 1)

# Combobox chọn chế đệ chơi
cbb_Type_Play = Combobox(frHang)
cbb_Type_Play['values'] = ('Chơi với người', 'Chơi với máy')
cbb_Type_Play.grid(row = 0, column = 2, padx = 30)
cbb_Type_Play.set('Chơi với người')
cbb_Type_Play.bind('<<ComboboxSelected>>', choose_Type)

# Frame chứa Entry lấy giá trị của cột
frCot = Frame(parent)
frCot.pack(pady = 5)
nCol = Label(frCot, text = "Nhập số cột:", width=15).grid(row = 0, column = 0)
e2 = Entry(frCot)
e2.insert(END, '10')
e2.grid(row = 0, column = 1)

# Label tạo khoảng trống làm đẹp giao diện XD
clone_Label = Label(frCot, text = "", width=28)
clone_Label.grid(row = 0, column = 2)

# Combobox chọn chơi X hay O
cbb_X_O = Combobox(frCot)
cbb_X_O['values'] = ('Đánh X', 'Đánh O')
cbb_X_O.set('Đánh X')

# Nút bắt đầu trò chơi
fr_Play_And_Depth = Frame(parent)
fr_Play_And_Depth.pack()
play = Button(fr_Play_And_Depth, text = "Bắt đầu chơi", command = btnPlay)
play.grid(row = 0, column = 0, padx = 30)
clone_Label1 = Label(fr_Play_And_Depth, text = "")
clone_Label1.grid(row = 0, column = 1, padx = 117)

# Chọn độ sâu của trò chơi
clone_Label_Depth = Label(fr_Play_And_Depth, text = "Độ khó trò chơi: ")
cbb_Depth = Combobox(fr_Play_And_Depth)
cbb_Depth['values'] = ('Cực dễ', 'Dễ', 'Trung bình', 'Khó')
cbb_Depth.set('Cực dễ')
cbb_Depth.bind('<<ComboboxSelected>>', choose_Level)
# Label cho biết lượt của ai
turnWho = Label(parent)
turnWho.pack()

# Frame chứa giao diện chính của trò chơi
fr = Frame(parent, padx = 20, pady = 20)
fr.pack()

# Hàm giữ cho giao diện hoạt động
parent.mainloop()
