def solution(genres, plays):
    answer = []
    
    # 장르 별 총 재생 수 hash
    total = {}
    
    # 장르 별 (재생 수, 고유번호) hash
    songs = {}
    
    for idx, (g,p) in enumerate(zip(genres, plays)):
        total[g] = total.get(g,0) + p
        if g not in songs:
            songs[g] = []
        songs[g].append((p,idx))
    
    
    # 총 재생 수 큰 장르부터 정렬
    genre_order = sorted(total.keys(), key=lambda g: total[g], reverse = True)
    
    
    # 각 장르에서 재생 수 내림차순, 고유번호 오름차순으로 정렬 후 최대 2개 선택
    for g in genre_order:
        songs[g].sort(key=lambda x: (-x[0],x[1]))
        answer.extend([idx for _, idx in songs[g][:2]])
    
    return answer