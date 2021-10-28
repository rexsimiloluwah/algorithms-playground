# IMPLEMENTATION OF THE SIEVE OF ERATHOSTHENES ALGORITHM IN PYTHON
class SOE:
    @staticmethod
    def compute_primes(N):
        """
            Computes all prime numbers less than N
        """
        boolean_array = [True]*(N + 1)
        # prime_nums = []
        for i in range(2, N + 1):
            if boolean_array[i] == True:
                yield i
                for j in range(i * i, N+ 1, i):
                    boolean_array[j] = False

if __name__ == "__main__":
    soe = SOE()
    print(list(soe.compute_primes(1000)))