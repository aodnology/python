from tkinter import *

window = Tk()

# title() : 윈도우창에 제목 표시
window.title("윈도우창연습")

#geometry() : 윈도우 크기 지정 
window.geometry("400x100")

#resizable() : 가로 세로의 크기 제어
window.resizable(width = False, height = False) # 초기값 고정
#window.resizable(width = True, height = True)  # 제어 가능
#window.resizable(width = "600", height = "600") 안됌


window.mainloop()