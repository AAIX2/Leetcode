# Approach-1 (Brute Force)
# T.C : add() - O(1), getProduct() - O(k)
# S.C : O(n) for the stream


class ProductOfNumbers:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        self.nums.append(num)

    def getProduct(self, k: int) -> int:
        ind = len(self.nums)-1
        prod = 1
        while k:
            prod*=self.nums[ind]
            k-=1
            ind-=1
        return prod


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)



# Approach-2 (Follow up optimal in O(1))
# T.C : O(1) for both methods
# S.C : O(n) for the stream

class ProductOfNumbers:

    def __init__(self):
        self.prefixProd = [1]
        self.size = 0
    def add(self, num: int) -> None:
        if num == 0:
            self.prefixProd = [1]
            self.size = 0
        else:
            self.prefixProd.append(self.prefixProd[-1]*num)
            self.size+=1
    def getProduct(self, k: int) -> int:
        if k>self.size:
            return 0
        return self.prefixProd[-1]//self.prefixProd[self.size-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)