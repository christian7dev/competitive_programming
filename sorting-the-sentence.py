class Solution:
    def sortSentence(self, s: str) -> str:
        sp = s.split(" ")
        List = []
        nList = []

        for x in range (len(sp)):
            List.append(0)
        for i in range (len(sp)):
            st = list(sp[i])
            loc = (int(st[-1]) -1 )
            List[loc] = sp[i]
        
        for i in range (len(List)):
            nst = list(List[i])
            nst.pop()
            nList.append(''.join(nst))
        return ' '.join(nList)
