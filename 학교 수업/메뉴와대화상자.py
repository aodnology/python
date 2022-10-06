from tkinter import *
from tkinter import messagebox

#함수 선언 부분
def f_open():
    messagebox.showinfo("메뉴선택","열기 메뉴를 선택함")

def f_exit():
    window.quit()
    window.destroy()

#메인 코드 부분
window = Tk() 
# 변수 window에 Tk() 대입

mainMenu = Menu(window)
# 메뉴자체 = Menu(부모윈도우)
window.config(menu = mainMenu)
#부모윈도우.config(menu = 메뉴자체)
fileMenu = Menu(mainMenu)                   
# 상위메뉴 = Menu(메뉴자체)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
#메뉴 자체.add_cascade(label = "상위메뉴텍스트", menu = 상위메뉴)
fileMenu.add_command(label = "열기", command = f_open)
# 상위메뉴.add_command(label = "하위메뉴1", command = 함수1)
fileMenu.add_separator()
#메뉴사이에 구분선을 넣음
fileMenu.add_command(label = "종료", command = f_exit)
# 상위메뉴.add_command(label = "하위메뉴2", command = 함수2)
window.mainloop()
# mainloop() : 이벤트가 발생(키보드나 마우스를 누르는 것)하는 것을 기다리는 함수
