# Approach-1 (Using Stack)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:    
        if x>=y:
            firstCh,secondCh = "a","b"
            f1,s1 = "b","a"
            score = x
            score1 = y
        else:
            firstCh,secondCh = "b","a"
            f1,s1 = "a","b"
            score = y
            score1 = x
        def getPoints(first,second,score,s):
            
            st = []
            res = 0
            for ch in s:
                if st and st[-1] == first and ch == second:
                        res+=score
                        st.pop()
                else:
                    st.append(ch)
            return [res,"".join(st)]
        val,s = getPoints(firstCh,secondCh,score,s)
        
        val1,st1 = getPoints(f1,s1,score1,s)
        return val+val1


# Approach-2 (Without Stack)
# T.C : O(n)
# S.C : O(1)    

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n = len(s)
        def removeSub(s,s1):
            i = j = 0
            while j<len(s):
                s[i] = s[j]
                if i>=1 and s[i] == s1[1] and s[i-1] == s1[0]:
                    i-=1  
                else:
                    i+=1  
                j+=1
            return "".join(s[:i])
        if x>y:
            s1 = "ab"
            s2 = "ba"
        else:
            s1 = "ba"
            s2 = "ab"
        ans = 0
        new = removeSub(list(s),s1)
        m = len(new)
        
        ans+=((n-m)//2)*max(x,y)
        # print(ans)
        new = removeSub(list(new),s2)
        # print(new)
        ans+=((m-len(new))//2)*min(x,y)
        return ans
        
            