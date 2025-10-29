class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        flag=True
        prev=0
        x=s.split()
        for i in x:
            if i.isdigit():
                if int(i)>prev:
                    prev=int(i)
                    continue
                else:
                    flag=False
                    break
            else:
                continue
        return flag
                    


        