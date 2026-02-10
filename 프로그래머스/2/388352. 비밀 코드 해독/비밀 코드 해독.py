from itertools import combinations

def solution(n, q, ans):
    answer = 0
    q_sets = [set(arr) for arr in q]
    m = len(q_sets)
    
    for comb in combinations(range(1,n+1), 5):
        ok = True
        
        for i in range(m):
            cnt = 0
            for x in q[i]:
                if x in comb:
                    cnt += 1
            if cnt != ans[i]:
                ok = False
                break
        if ok:
            answer += 1
        
    return answer