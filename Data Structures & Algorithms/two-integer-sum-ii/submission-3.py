class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx = 0
        while idx != len(numbers)-1:
            for n in numbers[idx + 1 :] :
                if numbers[idx] + n == target:
                    return [idx+1 , numbers.index(n)+1]
            idx +=1
        return False