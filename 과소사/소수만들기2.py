def solution(nums):
    answer = 0
    Sum = 0
    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                Sum = nums[i]+nums[j]+nums[k]
                for ii in range(2,Sum):
                    if Sum % ii == 0:
                        break
                else:
                    answer+=1

    return answer