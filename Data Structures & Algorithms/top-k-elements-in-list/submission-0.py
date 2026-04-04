class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        ar = []
        for num, c in count.items():
            ar.append([c, num])
        ar.sort()

        res = []
        while len(res) < k:
            res.append(ar.pop()[1])
        return res