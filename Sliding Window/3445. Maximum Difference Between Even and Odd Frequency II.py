# Approach  (Sliding Window)
# T.C : O(20 * n) ~= O(n)
# S.C : O(1)


class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)

        def getState(ele1,ele2):
            parity_a = ele1%2
            parity_b = ele2%2
            if parity_a == 0 and parity_b == 0:
                return 0
            elif parity_a and parity_b == 0:
                return 2
            elif parity_a == 0 and parity_b:
                return 1
            return 3
            

        res = float('-inf')
        # Trying all possible combinations from 0 to 4 where a!=b where a is the odd ele and b is the even ele
        for a in "01234":
            for b in "01234":
                if a == b:
                    continue
                # State for minPrev seen so far that stores smallest value for cnt_a - cnt_b

                stateMinPrev_a_b = [float('inf')]*5
                # cnt of a and b uptil ind r

                cnt_a = 0
                cnt_b = 0

                # cnt of a and b till prev ind
                prev_a = 0
                prev_b = 0

                # Starting the sliding window

                l = 0
                r = 0
                while r<n:
                    
                    cnt_a+=(1 if s[r] == a else 0)
                    cnt_b+=(1 if s[r] == b else 0)
                    
                    # Now we shrink from l and check until the substr is valid and we have we have at least 1 a since its odd and 2 b since its even
                    while r-l+1>=k and cnt_a-prev_a>=1 and cnt_b-prev_b>=2:
                        leftState = getState(prev_a,prev_b)
                        stateMinPrev_a_b[leftState] = min(stateMinPrev_a_b[leftState],prev_a-prev_b)
                        prev_a+=(1 if s[l] == a else 0)
                        prev_b+=(1 if s[l] == b else 0) 
                        l+=1
                        
                    
                    
                    rightState = getState(cnt_a,cnt_b)
                    bestLeftState = rightState^2
                    bestMinVal = stateMinPrev_a_b[bestLeftState]
                    if bestMinVal!=float('inf'):
                        res = max(res,(cnt_a-cnt_b)-bestMinVal)
                    r+=1
        return res