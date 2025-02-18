# Approach-1 - (Simple brute force)
# T.C : O(n * (n+1)!), (n+1)! permuations and n for matchesPattern()
# S.C : O(n+1) for result


from itertools import permutations

def matches_pattern(num, pattern):
    for i in range(len(pattern)):
        if (pattern[i] == 'I' and num[i] > num[i + 1]) or \
           (pattern[i] == 'D' and num[i] < num[i + 1]):
            return False
    return True

def smallest_number(pattern):
    n = len(pattern)
    num = ''.join(str(i) for i in range(1, n + 2))
    
    for perm in permutations(num):
        perm_str = ''.join(perm)
        if matches_pattern(perm_str, pattern):
            return perm_str
    
    return ""  # Should never reach here

# Approach-2 - (Recursion and backtracking)
# T.C : O(n * 9!), (n+1)! permuations and n for matchesPattern()
# S.C : O(n+1) for result

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        def solve(ind,res,vis):
            if ind == n:
                return True
            for i in range(1,10):
                if vis&(1<<i) == 0:
                    if (pattern[ind] == "I" and i>int(res[-1])) or (pattern[ind] == "D" and i<int(res[-1])):
                        res.append(str(i))
                        if solve(ind+1,res,vis^(1<<i)):
                            return True
                        res.pop()
                    elif pattern[ind] == "D" and i>int(res[-1]):
                        break
            return False
        for i in range(1,10):
            vis = 0
            res = [str(i)]    
            ans = solve(0,res,vis^(1<<i))
            if ans:
                return "".join(res)


# Approach-2 - (Simple using string as a stack) - You can use a stack<int> as well
# T.C : O(n)
# S.C : O(n) for the result

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        st = []
        res = []
        for i in range(n+1):
            st.append(i+1)
            if i == n or pattern[i] == "I":
                while st:
                    res.append(str(st.pop()))
        return "".join(res)



