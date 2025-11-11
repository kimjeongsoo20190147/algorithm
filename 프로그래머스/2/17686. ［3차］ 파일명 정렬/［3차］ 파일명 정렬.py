def solution(files):
    answer = []

    for idx, file in enumerate(files):
        num_start = 0
        while not file[num_start].isdigit():
            num_start += 1

        num_end = num_start

        while num_end < len(file) and file[num_end].isdigit():
            num_end += 1

        head = file[:num_start].lower()
        num = int(file[num_start:num_end])

        answer.append((head,num,idx,file))
        answer.sort(key = lambda x:(x[0], x[1], x[2]))
    return [i[3] for i in answer]