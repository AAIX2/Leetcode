# Approach-1 (Using set and substring find)
# T.C : O(n*L^2)
# S.C : O(n) //You can consider the length of each character as well - O(n*L)

from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_set = set(folder)
        result = []

        for curr_folder in folder:
            is_subfolder = False
            temp_folder = curr_folder

            while '/' in curr_folder:
                pos = curr_folder.rfind('/')
                curr_folder = curr_folder[:pos]

                if curr_folder in folder_set:
                    is_subfolder = True
                    break

            if not is_subfolder:
                result.append(temp_folder)

        return result
    

# Approach-2 (Using Sorting)
# T.C : O(n*logn) //You can consider the length of each character as well - O(n*L*logn)
# S.C : O(1)


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = set()
        for f in folder:
            cur = "/"
            flag = False
            for ch in f[1:]:
                if ch == "/":
                    if cur in res:
                        flag = True
                        break
                    cur+=ch
                else:
                    cur+=ch
            
            if not flag:
                res.add(f)
        return list(res)
             