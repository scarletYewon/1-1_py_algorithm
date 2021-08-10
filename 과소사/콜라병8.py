def solution(n, c, x):
    answer = 0
    drink = n
    new_c = c
    while True:
        new_c = n+c
        n = new_c //x
        c = new_c %x
        if n==0:
            break
        drink +=n
        answer = drink
    return answer