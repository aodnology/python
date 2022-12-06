print('1. 모듈')

def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print("타입이 달라 더할 수 없습니다.")
        return
    else:
        result = sum(a,b)
    return result

'''
if __name__ == "__main__":

1. 파일을 직접 실행시켰을 때 : 
    __name__ == "__main__"
    이 참이 되어 if문 다음 문장들이 수행된다

2. 대화형 인터프리터나 다른 파일에서 모듈을 불러올 경우
    __name__ == "__main__"
    이 거짓이 되어 if문 다음 문장들이 수행되지 않는다

외부에서 모듈을 불러와 인스턴스(함수)를 사용하려는 경우
 
'''
if __name__ == "__main__":
    print(safe_sum('a'),1)
    print(safe_sum(1,4))
    print(sum(10, 10.4))