# 클래스 선언

class userInfo:
    def __init__(self):
        self.name = input('이름: ')
        self.age  = input('나이: ')
        self.addr = input('주소: ')
    
    def show(self):
        print("이름 : {}, 나이 : {}, 주소 : {} 입니다.".format(self.name, self.age, self.addr))

# 클래스 호출
a = userInfo()
a.name
a.age
a.addr
a.show()

# 클래스 상속 (pass)
class userInfo2(userInfo): # class 클래스명(상속받는클래스명)
    def __init__(self):    # __init__ 상속받는 클래스의 내용은 사라지고 덮어쓰게 됨
        pass               # 덮어쓴 상태에서 pass를 선언 했기 때문에 아무것도 없는 내용이 됨.
                           # 추후 클래스 안에 특정 함수의 내용만 새로운 클래스에 상속하고 싶을 때 사용하면 될 것 같음.

# 클래스 상속 (super)
class userInfo3(userInfo):
    def __init__(self):
        super().__init__() # 상속받는 클래스안에 기존의 내용을 물려받음 / super() == class userInfo의 def __init__() 내용
        self.gender = input('성별 : ')
    def show(self):
        print(
            "이름 : {}\n나이 : {}\n주소 : {}\n성별 : {}".format(self.name, self.age, self.addr, self.gender)
            )
