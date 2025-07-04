def solution(answers):
    stu_1, stu_2, stu_3 = 0, 0, 0
    
    for i in range(len(answers)):
        if i % 5 == 0 and answers[i] == 1:
            stu_1 += 1
        elif i % 5 == 1 and answers[i] == 2:
            stu_1 += 1
        elif i % 5 == 2 and answers[i] == 3:
            stu_1 += 1
        elif i % 5 == 3 and answers[i] == 4:
            stu_1 += 1
        elif i % 5 == 4 and answers[i] == 5:
            stu_1 += 1
            
            
    for i in range(len(answers)):
        if i % 8 == 0 and answers[i] == 2:
            stu_2 += 1
        elif i % 8 == 1 and answers[i] == 1:
            stu_2 += 1
        elif i % 8 == 2 and answers[i] == 2:
            stu_2 += 1
        elif i % 8 == 3 and answers[i] == 3:
            stu_2 += 1
        elif i % 8 == 4 and answers[i] == 2:
            stu_2 += 1
        elif i % 8 == 5 and answers[i] == 4:
            stu_2 += 1
        elif i % 8 == 6 and answers[i] == 2:
            stu_2 += 1
        elif i % 8 == 7 and answers[i] == 5:
            stu_2 += 1
            
    for i in range(len(answers)):
        if i % 10 == 0 and answers[i] == 3:
            stu_3 += 1
        elif i % 10 == 1 and answers[i] == 3:
            stu_3 += 1
        elif i % 10 == 2 and answers[i] == 1:
            stu_3 += 1
        elif i % 10 == 3 and answers[i] == 1:
            stu_3 += 1
        elif i % 10 == 4 and answers[i] == 2:
            stu_3 += 1
        elif i % 10 == 5 and answers[i] == 2:
            stu_3 += 1
        elif i % 10 == 6 and answers[i] == 4:
            stu_3 += 1
        elif i % 10 == 7 and answers[i] == 4:
            stu_3 += 1
        elif i % 10 == 8 and answers[i] == 5:
            stu_3 += 1
        elif i % 10 == 9 and answers[i] == 5:
            stu_3 += 1
            
    stu = []
    stu.append(stu_1)
    stu.append(stu_2)
    stu.append(stu_3)

    max_value = max(stu)
    answer = [i+1 for i, value in enumerate(stu) if value == max_value]

    return answer