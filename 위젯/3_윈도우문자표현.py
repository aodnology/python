from tkinter import *
window = Tk()

# Label() : 윈도우에 문자를 표현하는 위젯
top_label = Label(window, text = "박수호")

middle_label = Label(
    #       글자            글꼴,크기 지정        글자색깔(foreground)
    window, text = "열심히", font=("바탕체",60), fg = "black"
    )

last_label = Label(
    #                          배경색(background)
    window, text = "시험 중입니다.", bg = "black", fg = "white",
# !위젯!의폭       넓이         위치지정,  글자의 크기가 아님 글자의 크리는 font로 설정  
    width = 20, height = 5, anchor = CENTER)

# pack() : 화면에 호출
top_label.pack()
middle_label.pack()
last_label.pack()
#blue_label.pack()
#money_label.pack()
#로또1등번호_label.pack()
window.mainloop()