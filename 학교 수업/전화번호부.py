call_num = {
    '경찰서':'112',
    '소방서':'119',
}

call_num['통신사'] = '114' # 자료 추가 문법
word = input("단어를 입력하세요 : ")
print(call_num.get(word, "없음"))