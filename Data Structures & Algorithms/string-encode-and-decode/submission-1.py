class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        
        for i in strs:
            res=res+str(len(i))+"#"+i #字符串的长度可能超过一位数
        
        return res

    def decode(self, s: str) -> List[str]:
        if s=="":
            return []

        res=[]

        pos=0

        while pos<len(s):            
            strlen=""
            nums=["0","1","2","3","4","5","6","7","8","9"]
            while s[pos] in nums:
                strlen=strlen+s[pos]
                pos+=1
            
            pos+=1 # 跳过#

            count=int(strlen)

            sub=s[pos:pos+count]
            res.append(sub)

            pos+=count
        
        return res