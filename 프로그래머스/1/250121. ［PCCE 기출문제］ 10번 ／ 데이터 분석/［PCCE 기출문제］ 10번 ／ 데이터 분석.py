def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    info_map = {"code":0, "date":1, "maximum":2, "remain":3}
    
    filtered_data = []
    ext_idx = info_map[ext]
    
    for item in data:
        if item[ext_idx] < val_ext:
            filtered_data.append(item)
            
    sort_idx = info_map[sort_by]
    
    def get_sort_key(item):
        return item[sort_idx]
    
    
    answer = sorted(filtered_data, key=get_sort_key)
    
    return answer