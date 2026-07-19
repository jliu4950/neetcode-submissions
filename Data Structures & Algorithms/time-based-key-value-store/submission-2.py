class TimeMap:

    def __init__(self):
        self.timeMap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if str in self.timeMap:
            self.timeMap[key].append([value,timestamp])
        else:
            self.timeMap[key]=self.timeMap.get(key,[])
            self.timeMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        elif self.timeMap[key][-1][1]<timestamp:
            return self.timeMap[key][-1][0] #情况1:找不到，且时间比所有时间大
        elif self.timeMap[key][0][1]>timestamp:
            return ""

        l=0
        r=len(self.timeMap[key])

        while l<r: #情况2:能找到
            m=(r-l)//2+l
            if self.timeMap[key][m][1]==timestamp:
                return self.timeMap[key][m][0]
            elif self.timeMap[key][m][1]>timestamp:
                r=m
            elif self.timeMap[key][m][1]<timestamp:
                l=m+1
        return self.timeMap[key][l-1][0]