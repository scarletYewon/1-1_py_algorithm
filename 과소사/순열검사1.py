def solution(arr):
    arr.sort()
    test_list = [i for i in range(1,len(arr)+1)]
    if test_list == arr:
        answer = True
    else:
        answer = False

    return answer
