def solution(v):
    answer = []
    xlist = []
    ylist = []
    for i in v:
        xlist.append(i[0])
        ylist.append(i[1])

    for i in xlist:
        if xlist.count(i) == 1:
            answer.append(i)
    for i in ylist:
        if ylist.count(i) == 1:
            answer.append(i)

    return answer