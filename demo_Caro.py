# Import thư viện tạo giao diện đơn giản
from tkinter import *
from tkinter import messagebox 

## turnXorO string chứa 'x' hoặc 'o' ( lượt tương ứng ), x, y là tọa độ của điểm vừa chọn
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
                return True, 'row'
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

# Hàm hover button
def on_enter(e):
    e.widget.config(bg='#99FFFF',fg = '#99FFFF')

#Hàm leave button
def on_leave(e):
    e.widget.config(bg='white', fg = 'white')

# Hàm khi nhấn vào button giao diện trò chơi
def clicked(btn, x, y):
    if numPlay[0] % 2 == 0:
        btn.unbind("<Leave>")
        btn.unbind("<Enter>")
        chessT[x][y] = 'x'
        btn.config(text = 'X',font=('Arial',15), bg = 'white', fg = 'black', state = 'disable')
        # Kiểm tra điều kiện thắng của X
        checkE, typeWin, sT, eN = checkEnd('x', x, y)
        if checkE:
            sT = int(sT)
            eN = int(eN)
            turnWho.config(text='X giành chiến thắng!')
            play.config(text = 'Chơi lại')
            buttons = fr.winfo_children()

            if typeWin == 'row':
                buttons[x * colT[0] + y].config(fg = 'red')
                for i in range(sT):
                    buttons[x * colT[0] + y + i + 1].config(fg = 'red')
                for i in range(eN):
                    buttons[x * colT[0] + y - i - 1].config(fg = 'red')
            elif typeWin == 'col':
                buttons[x * colT[0] + y].config(fg = 'red')
                for i in range(sT):
                    buttons[(x + i + 1) * colT[0] + y].config(fg = 'red')
                for i in range(eN):
                    buttons[(x - i - 1) * colT[0] + y].config(fg = 'red')
            elif typeWin == 'c1':
                buttons[x * colT[0] + y].config(fg = 'red')
                for i in range(sT):
                    buttons[(x + i + 1) * colT[0] + y + i + 1].config(fg = 'red')
                for i in range(eN):
                    buttons[(x - i - 1) * colT[0] + y - i - 1].config(fg = 'red')
            else:
                buttons[x * colT[0] + y].config(fg = 'red')
                for i in range(sT):
                    buttons[(x + i + 1) * colT[0] + y - i - 1].config(fg = 'red')
                for i in range(eN):
                    buttons[(x - i - 1) * colT[0] + y + i + 1].config(fg = 'red')


            for btnChild in buttons:
                btnChild.config(state = 'disable')
                try:
                    btnChild.unbind("<Leave>")
                    btnChild.unbind("<Enter>")
                except:
                    pass
            return


        if numPlay[0] == maxNumPlay[0]:
            turnWho.config(text='Hòa!')
            return
        turnWho.config(text = 'Tới lượt của o', font=('Arial, 15'))
    else:
        btn.unbind("<Leave>")
        btn.unbind("<Enter>")
        chessT[x][y] = 'o'
        btn.config(text = 'O',font=('Arial',15), bg = 'white', fg = 'black', state = 'disable')

        # Kiểm tra điều kiện thắng của O
        checkE, typeWin, sT, eN = checkEnd('o', x, y)
        if checkE:
            sT = int(sT)
            eN = int(eN)
            turnWho.config(text='O giành chiến thắng!')
            play.config(text = 'Chơi lại')
            buttons = fr.winfo_children()

            if typeWin == 'row':
                buttons[x * colT[0] + y].config(fg = 'red')
                for i in range(sT):
                    buttons[x * colT[0] + y + i + 1].config(fg = 'red')
                for i in range(eN):
                    buttons[x * colT[0] + y - i - 1].config(fg = 'red')
            elif typeWin == 'col':
                buttons[x * colT[0] + y].config(fg = 'red')
                for i in range(sT):
                    buttons[(x + i + 1) * colT[0] + y].config(fg = 'red')
                for i in range(eN):
                    buttons[(x - i - 1) * colT[0] + y].config(fg = 'red')
            elif typeWin == 'c1':
                buttons[x * colT[0] + y].config(fg = 'red')
                for i in range(sT):
                    buttons[(x + i + 1) * colT[0] + y + i + 1].config(fg = 'red')
                for i in range(eN):
                    buttons[(x - i - 1) * colT[0] + y - i - 1].config(fg = 'red')
            else:
                buttons[x * colT[0] + y].config(fg = 'red')
                for i in range(sT):
                    buttons[(x + i + 1) * colT[0] + y - i - 1].config(fg = 'red')
                for i in range(eN):
                    buttons[(x - i - 1) * colT[0] + y + i + 1].config(fg = 'red')

            for btnChild in buttons:
                btnChild.config(state = 'disable')
                try:
                    btnChild.unbind("<Leave>")
                    btnChild.unbind("<Enter>")
                except:
                    pass
            return
            
        if numPlay[0] == maxNumPlay[0]:
            turnWho.config(text='Hòa!')
            return
        turnWho.config(text = 'Tới lượt của x', font=('Arial, 15'))
    numPlay[0] += 1
    


# Hàm xóa hết giao diện bàn cờ khi ấn núi chơi 
def desChild():
    for widget in fr.winfo_children():
        widget.destroy()

# Hàm khi bấm núi chơi  
def btnPlay():
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

    # Khởi tạo bàn cờ và số lượt đầu trận
    numPlay.append(0)
    rowT.append(roW)
    colT.append(coL)
    maxNumPlay.append(roW * coL)
    play.config(text = 'Làm mới bàn cờ')
    for i in range(roW):
        d = []
        for j in range(coL):
            d.append(' ')
        chessT.append(d)
    turnWho.config(text = 'Tới lượt của x', font=('Arial, 15'))
    # Xây dựng giao diện trò chơi bằng mảng 2 chiều gồm roW * coL Button 
    buttons = [[Button(fr,font=('Arial', 15), width=5, height=2) for i in range(coL)] for i in range(roW)]
    for b in range(roW):
        for a in range(coL):
            # Text của Button chính là tọa độ của chúng
            buttons[b][a].config(bg = 'white', activebackground = 'white',width = 3, height = 1)
            buttons[b][a].bind("<Enter>", on_enter)
            buttons[b][a].bind("<Leave>", on_leave)
            buttons[b][a].config(command= lambda btn =  buttons[b][a], x = b, y = a: clicked(btn, x, y))
            buttons[b][a].grid( row = b, column = a)
# Bàn cờ mặc định chessT
chessT = []
# Số lượt đã chơi trong ván hiện tại
numPlay = []
# Số lượt đi tối đa
maxNumPlay = []
# Giá trị số hàng và cột của bàn cờ
rowT = []
colT = []

### Xây dựng giao diện game 
# Widget root cho giao diện
parent = Tk()
parent.title('Caro')

# Frame chứa Entry lấy giá trị của hàng
frHang = Frame(parent)
frHang.pack()
nRow = Label(frHang, text = "Nhập số hàng:",width=15).grid(row = 0, column = 0)
e1 = Entry(frHang)
e1.grid(row = 0, column = 1)

# Frame chứa Entry lấy giá trị của cột
frCot = Frame(parent)
frCot.pack()
nCol = Label(frCot, text = "Nhập số cột:", width=15,pady= 5).grid(row = 1, column = 0)
e2 = Entry(frCot)
e2.grid(row = 1, column = 1)

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