# Approach-1 (Brute Force)
# T.C : O(m*n)
# S.C : O(1)

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Continue removing occurrences of 'part' as long as it exists in 's'
        while part in s:
            # Find the index of the leftmost occurrence of 'part'
            part_start_index = s.find(part)

            # Remove the substring 'part' by concatenating segments before and after 'part'
            s = s[:part_start_index] + s[part_start_index + len(part) :]

        # Return the updated string after all occurrences are removed
        return s
    

# Approach-2 (Using Stack)
# T.C : O(m*n)
# S.C : O(m)

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(s)
        m = len(part)
        st = []
        for ch in s:
            if ch == part[-1] and len(st)+1>=m:
                removed = []
                j = m-2
                while st and j>=0:
                    if st[-1] == part[j]:
                        j-=1
                        removed.append(st.pop())
                    else:
                        
                        st+=removed[::-1]
                        st.append(ch)
                        break
            else:
                st.append(ch)
        return "".join(st)

                    
# Approach-3 (Using KMP)
# T.C : O(m+n)
# S.C : O(m+n)


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(s)
        m = len(part)
        def getLps(s):
            LPS = [0]*(len(s))
            LPS[0] = 0
            length = 0
            i = 1
            while i<len(s):
                if s[i] == s[length]:
                    length+=1
                    LPS[i] = length 
                    i+=1
                else:
                    if length:
                        length = LPS[length-1]
                    else:
                        LPS[i] = 0
                        i+=1
            return LPS
        lps = getLps(part)
        st = []
        prefixMatch = []
        for ch in s:
            st.append(ch)
            j = (0 if not prefixMatch else prefixMatch[-1])
            
            while j>0 and part[j]!=ch:
                j = lps[j-1]
            if ch == part[j]:
                j+=1
            prefixMatch.append(j)
            
            if j == m:
                st = st[:-m]
                prefixMatch = prefixMatch[:-m]
            
        return "".join(st)


                    