def solution(n, m, numbers):
    answer = 0
    check = set()
    for i in range(n, m + 1):
        for j in numbers:
            if i % j == 0 and i not in check:
                check.add(i)
                answer += i

    return answer