print('5. 클래스')
# 클래스 : 똑같은 무엇인가를 계속해서 만들어낼 수 있는 설계 도면 (뽑기의 틀)
# 인스턴스 : 클래스에 의해서 만들어진 피조물 (틀 모양의 뽑기)
class Calculator:
    def __init__(self):
        self.result = 0
    
    def adder(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal1.adder(3))
print(cal1.adder(7))

print('5-2. 클래스의 간단한 예')
class simple:
    pass

a = simple() # a : 인스턴스
#인스턴스 = 클래스

# print('5-3. 객체와 인스턴스의 차이')
# 인스턴스 : 클래스에 의해서 만들어진 객체
# a = class() 이렇게 만들어진 객체를 인스턴스라고도 함
# a 라는 객체는 class의 인스턴스이다
# 인스턴스 : 특정 객체(a)가 어떤 클래스의(class)의 객체인지를
#          관계 위주로 설명할 때 사용됨
# a는 '인스턴스' 보다는 a는 '객체'라는 표현이 어울림
# a는 'class의 객체'보다는 a는 'class의 인스턴스'라는 표현이 어울림

print('5-3. 이야기 형식으로 클래스 기초 쌓기')
class Service:
    secret = "나는 박수호."

class Service2:
    secret = "나는 박수호."
    def sum(self, a, b):
        result = a + b
        print("%s + %s = %s" %(a, b, result))

sooho = Service2()
a = sooho.secret
print(a)
sooho.sum(1,1)

class Service3:
    secret = "나는 박수호"
    def setname(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." %(self.name, a, b, result))

sooho = Service3()
sooho.setname("박수호")
sooho.sum(2,3)