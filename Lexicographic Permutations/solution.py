# Problem Description => https://bit.ly/ucode-1
## References :- 
# https://en.wikipedia.org/wiki/Factorial_number_system,  youtube
# Great problem though !!, I hope this solution suffices
import time 
class LexicographicPermutations:
    def __init__(self, discrete_digits, perm_index):
        """
            Args (num, perm_index)
            ==========================================================
            num (str) => Discrete set of digits
            perm_index(int) => The index used to compute the Nth permutation
        """
        self.discrete_digits = discrete_digits
        self.perm_index = perm_index
    
    
    def convert_to_factorial_number_system(self, n):
        """
            Desc : This function converts the perm_index (i.e Nth permutation) to a factoradic
            Args : (n)
            ===================================================================
            n (int) => perm_index
            Returns (int) : Computed factoradic based on the factorial discrete_digitsber system algorithm

        """
        factoradic = [0]*len(str(self.discrete_digits))
        x = 1
        while n-1 >= 0:
            n, factoradic[len(str(self.discrete_digits)) - x] = divmod(n, x)
            x += 1
        return(factoradic)

    def compute_nth_perm(self):
        """
            Desc : This function computes the Nth permutation for the discrete_digits based on the factoradic of the Index
            Args : factoradic (Computed factoradic from the previous function)
            Returns (int) : Final result
        """
        factoradic = self.convert_to_factorial_number_system(int(self.perm_index) - 1)
        discrete_digits_list = list(str(self.discrete_digits))
        output = []

        for j in range(len(discrete_digits_list)):
            output.append(discrete_digits_list.pop(factoradic[j]))
        return int("".join(output))


if __name__ == "__main__":
    discrete_digits =  input()
    perm_index = int(input())
    start = time.time()
    lexicographicorder = LexicographicPermutations(discrete_digits,perm_index)
    print(lexicographicorder.compute_nth_perm())
    end = time.time()
    print("===================================================================")
    print("".join(["The Elapsed time for this test case is :- ", str(end - start)," seconds"]))



    


 