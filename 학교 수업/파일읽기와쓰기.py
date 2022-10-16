print("readline() : line별로 파일 읽기")
f = open("새파일.txt",'r') # r : 읽기 전용
line = f.readline()      # readline : 파일의 첫번째 줄 읽음
print(line)
f.close()

# while 모든 라인 읽기
print('while')
f = open("새파일.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line, end="")
f.close()

# for 모든 라인 읽기
print('for')
f = open("새파일.txt",'r')
lines = f.readlines()
for line in lines:
    print(line, end="")
f.close()

print("read() : 파일 전체 내용 읽기")
f = open("새파일.txt", 'r')
a = f.read()
f.close()
print(a)

print("파일에 새로운 내용 추가하기 'a'")
f = open("새파일.txt",'a') # 'a' : 파일의 내용은 그대로 유지하면서 새로운 값만 추가함
for i in range(11, 21):
    a = "%d번째줄입니다\n" %i
    f.write(a)
f.close

print("파일 자동으로 열고 닫기 : with ")
#with open("파일명", "조건") as 변수:
#   변수.write("내용")

with open('test.txt','w') as f:
    f.write("with문을 사용해서 파일에 입력하고있습니다.")

with open('test.txt','r') as f:
    a = f.read()
    print(a)