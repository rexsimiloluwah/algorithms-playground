# SOLUTION TO FIBONACCI SEQUENCES PROBLEMS 
class Solution:
    def compute_fibonacci_term(self, N):
        """ This function computes an Nth term in fibonacci sequence recursively """
        if N <= 1:
            return N
        return self.compute_fibonacci_term(N -1) + self.compute_fibonacci_term(N -2)

    def compute_fibonacci_sequence(self, N):
        """ This function computes an N-long fibonacci sequence """
        fib_seq = []
        for _ in range(N):
            fib_seq.append(self.compute_fibonacci_term(_))
        return fib_seq

    @staticmethod
    def compute_fibonacci_sequence_ptimized(N):
        """ optimized solution """
        i,j = 0,1
        fib_seq = [i,j]
        while len(fib_seq) <= N:
            fib_seq.append(fib_seq[i] + fib_seq[j])
            i+= 1
            j+= 1
        
        return fib_seq


if __name__ == "__main__":
    solution = Solution()
    print(solution.compute_fibonacci_term(30))  #30
    print(solution.compute_fibonacci_sequence_optimized(100)[30]) 

