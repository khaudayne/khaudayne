# Import thư viện tạo giao diện đơn giản
import random
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox 

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

# Hàm lấy tọa độ một điểm chưa được chọn ngẫu nhiên
def get_Point():
    while True:
        x = random.randint(0, rowT[0] - 1)
        y = random.randint(0, colT[0] - 1)
        if not checkChessT[x][y]:
            return x, y

# Hàm xuất hiện chọn đánh X hay O khi chơi với máy
def choose_Type(e):
    typeGame = e.widget.get()
    try:
        if typeGame == 'Chơi với máy':
            clone_Label.grid_forget()
            cbb_X_O.grid(row = 0, column = 3 , padx = 30)
        else:
            cbb_X_O.grid_forget()
            clone_Label.grid(row = 0, column = 2)
    except:
        pass

# Hàm hover button
def on_enter(e):
    e.widget.config(bg='#99FFFF',fg = '#99FFFF')

#Hàm leave button
def on_leave(e):
    e.widget.config(bg='white', fg = 'white')

# Hàm khi nhấn vào button giao diện trò chơi
def clicked(btn, x, y):
    if checkChessT[x][y]:
        return
    checkChessT[x][y] = True
    if numPlay[0] % 2 == 0:
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
            x, y = get_Point()
            buttons = fr.winfo_children()
            btn = buttons[x * colT[0] + y]
            numPlay[0] += 1
            clicked(btn, x, y)
            return
        else:
            turnWho.config(text = 'Tới lượt của o', font=('Arial, 15'))

        
    else:
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
            x, y = get_Point()
            buttons = fr.winfo_children()
            btn = buttons[x * colT[0] + y]
            numPlay[0] += 1
            clicked(btn, x, y)
            return
        elif typeG[0] == 'Chơi với máy' and choose_X_O[0] == 'Đánh X':
            turnWho.config(text = 'Tới lượt của bạn', font=('Arial, 15'))
        else:
            turnWho.config(text = 'Tới lượt của x', font=('Arial, 15'))

    numPlay[0] += 1
    
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
    numPlay[0] = 0
    rowT[0] = roW
    colT[0] = coL
    maxNumPlay[0] = roW * coL - 1
    play.config(text = 'Làm mới bàn cờ')
    for i in range(roW):
        for j in range(coL):
            chessT[i][j] = ' '
            checkChessT[i][j] = False
    turnWho.config(text = 'Tới lượt của x', font=('Arial, 15'))
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
        x, y = get_Point()
        buttons = fr.winfo_children()
        btn = buttons[x * colT[0] + y]
        clicked(btn, x, y)

# Bàn cờ mặc định chessT
chessT = [[' ' for i in range(100)] for i in range(100)]
# Đánh dấu các điểm đã chọn
checkChessT = [[False for i in range(100)] for i in range(100)]
# Số lượt đã chơi trong ván hiện tại
numPlay = [0]
# Số lượt đi tối đa
maxNumPlay = [0]
# Giá trị số hàng và cột của bàn cờ
rowT = [0]
colT = [0]
# Thể loại chơi
typeG = [0]
# Đánh X hay O
choose_X_O = [0]

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
frCot.pack()
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
play = Button(parent, text = "Bắt đầu chơi", command = btnPlay)
play.pack()

# Label cho biết lượt của ai
turnWho = Label(parent)
turnWho.pack()

# Frame chứa giao diện chính của trò chơi
fr = Frame(parent, padx = 20, pady = 20)
fr.pack()

# Hàm giữ cho giao diện hoạt động
parent.mainloop()
