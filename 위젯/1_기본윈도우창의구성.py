# tkinter : GUI 관련 모듈을 제공하는 표준 윈도우 라이브러리
from tkinter import *

# 기본 윈도우 반환하기 : Tk()
window = Tk()

# mainloop()는 이벤트 메시지 루프로서 
# 키보드나 마우스 혹은 화면 Redraw와 같은 
# 다양한 이벤트로부터 오는 메시지를 받고 전달하는 역활을 한다.
window.mainloop()