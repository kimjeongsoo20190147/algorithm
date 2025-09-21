def solution(record):
    answer = []
    idmap = {}
    
    
    for str in record:
        strlist = str.split()
        cmd = strlist[0]
        if cmd == 'Enter' or cmd == 'Change':
            id = strlist[1]
            name = strlist[2]
            idmap[id] = name
            
    for str in record:
        strlist = str.split()
        cmd = strlist[0]
        if cmd == 'Enter':
            id = strlist[1]
            answer.append(idmap[id] + '님이 들어왔습니다.')
        elif cmd == 'Leave':
            id = strlist[1]
            answer.append(idmap[id] + '님이 나갔습니다.')
    
    return answer