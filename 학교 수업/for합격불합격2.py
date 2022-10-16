marks = [90,25,67,45,80]
num = 0
for mark in marks:
    num = num + 1
    if mark < 60:
        continue
    else:
        print("%d번 학생 합격입니다."%num)