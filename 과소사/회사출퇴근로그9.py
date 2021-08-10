def solution(logs):
    d = set()
    for i in logs:
        if i in d:
            d.remove(i)
        else:
            d.add(i)
    answer = sorted(d)
    return answer