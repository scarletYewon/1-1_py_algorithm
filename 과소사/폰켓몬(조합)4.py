def solution(nums):
    answer = 0
    values = len(nums) // 2
    values_list = []
    for i in range(len(nums)):
        if nums[i] not in values_list:
            values_list.append(nums[i])
    if len(values_list) >= values:
        answer = values
    else:
        answer = len(values_list)
    return answer