# SOLUTION TO FIBONACCI SEQUENCES PROBLEMS 
import time
class Solution:

    def computeFibonacciTerm(self, N):
        """
            This function computes an Nth term in fibonacci sequence recursively
        """
        if N <= 1:
            return N
        return self.computeFibonacciTerm(N -1) + self.computeFibonacciTerm(N -2)

    def computeFibonacciSequence(self, N):
        """
            This function computes an N-long fibonacci sequence
        """
        fib_seq = []
        for _ in range(N):
            fib_seq.append(self.computeFibonacciTerm(_))
        return fib_seq

    @staticmethod
    def computeFibonacciSequenceOptimized(N):
        """
            optimized solution
        """
        i,j = 0,1
        fib_seq = [i,j]
        while len(fib_seq) <= N:
            fib_seq.append(fib_seq[i] + fib_seq[j])
            i+= 1
            j+= 1
        
        return fib_seq


if __name__ == "__main__":
    solution = Solution()
    print(solution.computeFibonacciTerm(30))  #3
    # print(solution.computeFibonacciSequenceOptimized(100))  #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

