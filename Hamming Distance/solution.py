# Simple implementation of Hamming distance 
class HammingDistance:
    @staticmethod
    def compute(x, y):
        """
            Args:-
            ------------------------------------------------------
            x (int), y(int)
            Returns :- 
            ------------------------------------------------------
            int :- Computed Hamming distance
        """

        # Simple solution (Compute the binary equivalent of the XOR of the two integers)
        xor = bin(x ^ y).split('b')[-1]
        return xor.count('1')

if __name__ == "__main__":
    h = HammingDistance()
    print(h.compute(12,15))

