import sys
'''
cmd나 terminal에서 
python memo.py -a "Life is too short" 입력시 메모 추가
python memo.py -v

-a : 프로그램 실행 옵션 / 메모 추가
-v : 메모 출력
'''

option = sys.argv[1] # 프로그램 실행 옵션 / 메모 추가 ( -a )
# sys.argv
# 프로그램 실행 시 입력된 값을 읽어 들일 수 있는 파이썬 라이브러리
if option =='-a':
    memo = sys.argv[2]   # 메모 내용 ("Life is too short")
    f = open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()
# -v 옵션의 경우 파일 읽고 출력하기    
elif option == '-v':
    f = open('memo.txt')
    memo = f.read() # 파일 읽고
    f.close()
    print(memo)     # 출력
