# 순차 탐색 알고리즘 O(N)
# slist

def Sequential_Search(list, target):
    size = len(list)
    for i in range(0, size):
        if target == list[i]:
            return i+1
    
    return -1

rlist = [1,2,3,4,5,6]
print(Sequential_Search(rlist, 5))
