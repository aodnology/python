# 기본형
# 파일 객체 = open(파일이름, 파일 열기 모드)
# 파일 열기모드 (r,w,a)
# r : 읽기 모드
# w : 쓰기 모드
# a : 추가 모드 (파일의 마지막에 새로운 내용을 추가할 때 사용) 

f = open("새파일.txt",'w') # "c:\python\새파일" 과 같이 경로 지정도 가능

for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)               # data를 파일 객에 f에 씀
f.close()


