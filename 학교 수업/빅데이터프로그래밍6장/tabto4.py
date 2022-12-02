'''
ppt 21page

문서 파일을 읽어서 그 문서 파일내에 있는 탭(tab)을 
공백 4개로 바꾸기

필요 기능 : 파일 읽기 , 문자열 변경
입력 받는 값 : 탭을 포함한 문서 파일
출력 값 : 탭이 공백으로 수전된 문서 파일

tabto4.py = 파이썬 프로그램
src = 탭을 포함하고 있는 원본 파일
dst = 파일 내의 탭을 공백 4개로 변환한 결과 저장할 파일
'''

import sys

src = sys.argv[1] # 탭 포함 파일
dst = sys.argv[2] # 공백으로 변경하여 저장할 파일

f = open(src)
tab_content = f.read() # src 파일의 내용을 읽어 변수에 저장
f.close()

space_content = tab_content.replace("\t", " "*4)
# src 내용이 들어가있는 변수 tab_content를 
# replace() 함수를 사용하여 탭을 공백*4로 변경하여 변수에 저장

f = open(dst)           # 변경될 내용을 저장할 파일을 열고
f.write(space_content)  # write() 를 사용하여 입력할 내용이 담긴 변수를 대입하여 쓰기
f.close()