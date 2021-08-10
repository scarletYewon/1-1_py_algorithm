def solution(no, works):
    result = 0
    for _ in range(no):
        works.sort()
        if works[-1] == 0:
            break
        works[-1] -= 1

    for i in works:
        result += i ** 2

    return result