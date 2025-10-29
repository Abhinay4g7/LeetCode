class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        flag=True
        prev=0
        for i in s.split():
            if i.isdigit():
                if int(i)<=prev:
                    flag=False
                    break
                prev=int(i)
        return flag
                    


        