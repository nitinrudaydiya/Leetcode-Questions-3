class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        a = []
        for i in bank :
            c = i.count("1")
            if c>0:
                a.append(c)


        if len(a)==1 or len(a)==0:
            return 0
        else:
            count = 0
            for i in range(len(a)-1):
                count+=a[i]*a[i+1]
            return count