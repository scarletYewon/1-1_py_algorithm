def solution(arr):
    answer = []
    for i in range(len(arr)):
        answer.append(arr[i])
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                answer.pop()
                break
            else:
                break
    return answer