# data : [코드번호, 제조일, 최대수량, 현재수량]
# ext : 기준, val_ext : 기준 값, sort_by : 정렬
# ext, sort_by : code(코드번호), date(제조일), maximum(최대수량), remain(현재수량)
def solution(data, ext, val_ext, sort_by): 
    col = ['code', 'date', 'maximum', 'remain']
    data = [d for d in data if d[col.index(ext)] <= val_ext]
    data = sorted(data, key=lambda x: x[col.index(sort_by)])
    return data