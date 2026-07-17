class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for words in strs:
            sorted_word = "".join(sorted(words))
            if sorted_word not in results.keys():
                results[sorted_word]= [words]
            else :
                results[sorted_word].append(words)
        return list(results.values())