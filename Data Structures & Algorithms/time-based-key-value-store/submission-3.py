from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.TimeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeMap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        nums = self.TimeMap.get(key,[])
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (r - l) // 2 + l
            if nums[m][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1
        return nums[r][1] if r != -1 else ""
