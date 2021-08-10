def solution(n,m):
    answer = 0
    for i in range(n,m+1):
        string = str(i)
        for j in range(len(string)//2):
            if not string[j] == string[len(string)-1-j]:
                break
        else:
            answer+=1

    return answer