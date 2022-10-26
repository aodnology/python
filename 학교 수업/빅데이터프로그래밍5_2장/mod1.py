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