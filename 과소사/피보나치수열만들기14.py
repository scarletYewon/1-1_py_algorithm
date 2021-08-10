dic = {0: 0, 1: 1}

def fibo(n):
    if n in dic:
        return dic[n]

    dic[n] = fibo(n - 1) + fibo(n - 2)
    return dic[n]

def solution(n):
    answer = float(fibo(n))
    return answer