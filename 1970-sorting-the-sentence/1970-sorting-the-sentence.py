class Solution:
    def sortSentence(self, s: str) -> str:
        x=s.split()
        copy=list(x)
        for i in x:
            copy[int(i[len(i)-1])-1]=i[:-1]
        res=" ".join(copy)
        return res    
        