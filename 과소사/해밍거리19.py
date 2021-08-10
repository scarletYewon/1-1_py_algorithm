from hashlib import md5


def solution(string1, string2):
    answer = 0
    string1 = md5(bytes(string1, encoding='utf-8'))
    string2 = md5(bytes(string2, encoding='utf-8'))

    for i in range(len(string1.hexdigest())):
        if string1.hexdigest()[i] != string2.hexdigest()[i]:
            answer += 1

    return answer