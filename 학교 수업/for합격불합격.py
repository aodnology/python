score = [90, 25, 67, 45, 80]
num = 0
for scores in score:
    num = num + 1
    if scores >=60:
        print("%d번 합격"%num)
    else:
        print("%d번 불합격"%num)

