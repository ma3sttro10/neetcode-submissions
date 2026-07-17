class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = {}
        for num in nums:
            if num not in results :
                results[num] = 1
            else :
                results[num] += 1
        sorted_result = dict(sorted(results.items(),key=lambda kv:kv[1],reverse = True))
        lst = list(sorted_result.keys())
        return lst[:k]