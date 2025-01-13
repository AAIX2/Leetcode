pat = "at"
text = "attention"
length = 0
LPS = [0]*len(pat)
LPS[0] = 0
i = 1
while i<len(pat):
    if pat[length] == pat[i]:
        length+=1
        LPS[i] = length
        i+=1
    else:
        if length>0:
            length = LPS[length-1]
        else:
            LPS[i] = 0
            i+=1
def KMP(text,pattern):
    n = len(text)
    m = len(pattern)
    i = j = 0
    ans = -1
    while i<n:
        if text[i] == pattern[j]:
            i+=1
            j+=1
        if j == m:
            ans = i-j
            j = LPS[j-1]
        elif text[i]!=pattern[j]:
            if j-1>=0:
                j = LPS[j-1]
            else:
                i+=1
    return ans

print(KMP(text,pat))
# T.C. : O(n+m)
# S.C. : O(m)
