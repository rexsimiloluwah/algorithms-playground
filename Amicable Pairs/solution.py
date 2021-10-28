# SOLUTION FOR AMICABLE PAIRS PROBLEM 
from functools import reduce
class Solution:
    def find_factors(self, N):
        """
            Desc. : Basic algorithm to find the sum of all proper divisors of a number
            Args (int) : N
            Returns (int) : sum of the list of factors
        """
        factors = set(reduce(list.__add__, [[i, N//i] for i in range(1, int(N**0.5)+ 1) if N % i == 0]))
        factors.remove(N)
        return sum(list(factors))

    def is_amicable(self, a,b):
        """
            Desc. : Checks for *amicability based on the given condition
            Args (int,int): a,b
            Returns (Boolean)
        """
        if (self.find_factors(a) == b) and (self.find_factors(b) == a):
            return True
        return False

if __name__ == "__main__":
    solution = Solution()
    a = int(input())
    b = int(input())

    print(solution.is_amicable(a,b))