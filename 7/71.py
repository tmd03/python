nums = [4,7,10,2,4,7,0,2,7,3,9]
print(f'nums : {nums}')
print(f'nums length : {len(nums)}')

searchData = int(input('input search Num : '))
searchIdx = []

nums.append(searchData)

n=0
while True:
    if nums[n] == searchData :
        if n != len(nums) -1:
            searchIdx.append(n)
        else:
            break

    n += 1

print(f'nums : {nums}')
print(f'nums length : {len(nums)}')
print(f'searchIdxcnt: {len(searchIdx)}')

print('-'*20)
nums = [4,10,22,5,0,17,7,11,9,61,88]
nums.sort()
print(nums)

searchD = int(input('찾는 숫자 입력: '))
searchI = -1

staIdx = 0
endIdx = len(nums)-1
midIdx = (staIdx + endIdx) // 2
midVal = nums[midIdx]

while searchD <= nums[len(nums)-1] and searchD >= nums[0]:
    if searchD > midVal:
        staIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')
    elif searchD < midVal:
        endIdx = midIdx
        midIdx = (staIdx + endIdx) // 2
        midVal = nums[midIdx]
        print(f'midIdx: {midIdx}')
        print(f'midVal: {midVal}')
    elif searchD == midVal:
        searchI = midIdx
        break

print(f'search Idx : {searchI}')