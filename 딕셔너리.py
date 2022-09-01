# 딕셔너리 : java의 hashmap과 같이 키(key)와 값(value)으로 이루어진 자료형

myfriend = {
    'name' : 'cokkiry',
    'age' : '25',
    'job' : 'tsu'
}
print(myfriend)
# print(type(myfriend))

# 입력 된 데이터 변경
myfriend['age']='1000'
print(myfriend)
print(myfriend.keys())
print(myfriend.values())
print(myfriend.items())