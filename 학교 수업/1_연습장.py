def sum_many(*a):
    sum=0
    for i in a:
        sum += i
    return sum

a = sum_many(1,2,3,4,5,6,7,8,9,10)
print(a)

def sum_choice(choice, *a):
    if choice == sum:
        res = 0
        for i in a:
            res += i
    elif choice == mul:
        res = 1
        for i in a:
            res *= i
    return res

result = [ x*y for x in range(2,10) for y in range(2,10)]
print(result, end=" ")

for i in range(2, 10):
    for j in range(1,10):
        print(i*j, end=" ")
    print("")


a = [1,2,3,4]
result=[]
for i in a:
    result.append(i*3)

print(result)

result = [i * 3 for i in a if i % 2 ==0]
print(result)