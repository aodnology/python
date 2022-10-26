print('1. 클래스')
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

print('1-2. 클래스의 간단한 예')
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

print('1-3. 이야기 형식으로 클래스 기초 쌓기')
class Service:
    secret = "나는 박수호."

class Service2:
    secret = "나는 박수호."
    def sum(self, a, b):
        result = a + b
        print("%s + %s = %s" %(a, b, result))

# 클래스 안에 변수 대입하기
# [변수] = [클래스()]
# [대입할변수] = [클래스를대입한변수].[클래스안의변수]
sooho = Service2()
a = sooho.secret 

print(a)
sooho.sum(1,1)

print('1-4. self 제대로 알기')
# "[이름]님 1 + 2 = 3 입니다" 처럼 결과값을 내는 것이 목적
class Service3:
    secret = "나는 박수호"
    def setname(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." %(self.name, a, b, result))
#sum함수에 self.name을 출력문에 삽입하여 사용자의 이름을 출력하게한다.

sooho = Service3() 
# sooho라는 아이디를 가진 사람이 이 서비스 업체의 sum이라는 서비스를 이용하겠따고 요청한다는 의미
sooho.setname("박수호")
# sooho라는 아이디를 가진 사람이 자신의 이름은 박수호임을 서비스 업체에 알려줌
# setname 함수를 통해 이름을 정의하여 앞으로 sooho라는 아이디와 박수호라는 이름은 연결해 주는것이
# self이다.
sooho.sum(2,3)
#더하기 서비스 이용
#setname을 통해 그 사람의 이름을 부여하는 과정이 끝남

print('1-5. __init__')
# babo = Service()
# babo.sum(1, 1)
# 위와 같이 입력하면 babo.setname("나바보")와 같은 이름을 넣어 주는 과정이 생략되어 문제가 생긴다
# 아이디를 부여할때 그 사람의 이름을 입력 받아야만 아이디를 부여해 주는 방식으로 바꾸면
# setname 함수를 이용하는 과정을 생략할 수 있다.(__init__의 역할)

class Service4:
    secret = "나는 박수호."
    def __init__(self, name): # setname 함수 이름인 setname이 __init__으로 바뀜
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s 입니다." %(self.name, a, b, result))

sooho = Service4("박수호") # __init__함수를 통해 아이디를 부여 받을 때 이름까지 함께 임력함
sooho.sum(1, 1)
# __init__을 통해 기존에
# sooho = Sevice4()           
# sooho.setname("박수호") 
# 위 코드가
# sooho = Service4("박수호") 로 대입가능하게 됨

print('1-6. 사칙연산 클래스 만들기')
# 아무 기능 없는 빈 클래스
class FourCal1:
    pass

a = FourCal1() # 빈클래스도 객체를 만들 수 있다.
print(type(a))

#객체에 숫자 지정할 수 있게 만들기
class FourCal2:
    def setdata(self, first, second): # Fourcal2 클래스에 setdata 함수 생성
        self.first = first            # 클래스해서 함수를 다른말로 [메소드]라고도 함.
        self.second = second

a = FourCal2()
a.setdata(4, 2)
# [ self : a ](객체) , [ first : 4 ] , [second : 2]
# setdata의 입력 인수는 self, first, second로 총 3개이지만 a.setdata(4, 2)처럼
# 2개의 입력값만 주어도 a라는 인스턴스가 setdata 함수의 첫 번째 입력은 받는 변수인 self에 대입 됨

print('2. 메소드의 다른 호출 방법')

#[클래스명].[메소드]([객체],[인수],[인수])

FourCal2.setdata(a, 4, 2)
# 1. [클래스명].[메소드] 형태로 호출할 때 
#     :객체 a를 입력 인수로 반드시 self자리에 넣어줘야 함

a.setdata(4, 2)
# 2. [객체].[메소드] 형태로 호출할 때는 
#    :첫 번째 입력 인수(self)를 반드시 생략해야함

print('2-2. 메소드의 수행문')
# setdata 메소드의 수행문
class FourCal3:
    def setdata(self, first, second): # Fourcal2 클래스에 setdata 함수 생성
        self.first = first            # 클래스해서 함수를 다른말로 [메소드]라고도 함.
        self.second = second

# 위 클래스에서 setdata 메소드의 수행문 구조 파악
a = FourCal3()
a.setdata(4, 2)

# 위와 같이 대입을 했을때
# self.first = 4
# self.second = 2

# a.setdata(4, 2) : [객체].[메소드](인수, 인수)
# 형태 이므로
# a.first = 4
# a.second =2 
# 임을 알 수 있다.

print(a.first)  #4
print(a.second) #2

b = FourCal3()
b.setdata(5,3)
print(b.first)  #5
print(b.second) #3

# a와 b라는 객체 모두 first라는 변수를 가지고 있지만
# 변수의 값은 각기 다르다 (객체간 변수가 같아도 서로 영향을 받지 않음)

print('2-3. 더하기 기능 만들기')

class FourCal4:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result

FourCal4.setdata(a, 4, 2)
# ==
a = FourCal4()
a.setdata(4,2)
print(a.sum())

# 클래스 안에 함수를 사용하기 위해선
# 객체에 클래스를 대입시켜 주어야함

print('2-4. 사칙연산')
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        res = self.first + self.second
        return res
    def mul(self):
        res = self.first * self.second
        return res
    def sub(self):
        res = self.first - self.second
        return res    
    def div(self):
        res = self.first / self.second
        return res

# [결과] = [객체.인수] [연산식] [객체.인수]

a = FourCal()
a.setdata(4,2)
print(a.sum())
print(a.mul())
print(a.sub())
print(a.div()) 
#print(type(a.div())) 
# #나누기의 경우 자동으로 float으로 type이 변하는지 물어보기
