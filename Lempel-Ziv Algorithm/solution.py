# Author: - TheBlackdove (Similoluwa Okunowo)
import time

class LempelZivCoding:
    def __init__(self,input_sequence:str):
        self.sequence=input_sequence
        self.phrases=[]
        
    @staticmethod
    def dec2bin(number:int):
        """
            Description: Utility function to convert a decimal number to binary
            Args: The Decimal number (int)
        """
        bin=[]
        while number > 0:
            x,y=divmod(number,2)
            number=x
            bin.append(str(y))
        return "".join(reversed(bin))
    
    # Lempel-Ziv Coding Step 1: - Parse the input sequence into unique phrases
    def parse_sequence(self):
        sequence=list(self.sequence)
        word = ""
        dictionary=[]
        result = []
        i=0
        while len(sequence)>0:
            wc = sequence[0]
            word=word+wc 
            if word in dictionary:
              pass
            else:
              dictionary.append(word)
              word=""
            sequence.pop(0)
        self.phrases=dictionary
        return dictionary
    
    def generate_codewords(self):
        codewords=[]
        for phrase in self.phrases:
            if len(phrase)==1:
                codeword=phrase
            else:
                codeword=self.dec2bin(self.phrases.index(phrase[0:-1])+1)+phrase[-1]
            codewords.append(codeword)
        max_len= len(max(self.phrases,key=len))
        codewords=map(lambda x:x.zfill(max_len),codewords)
        return list(codewords)
    
#Testing
# When Input Sequence = 001011011100010101111
start = time.time()
lempelziv = LempelZivCoding("001011011100010101111")
print('The Unique Phrases are: - ', lempelziv.parse_sequence())
print('The Lempel-Ziv Encoded words are: - ',lempelziv.generate_codewords())
end = time.time()
print(end-start, 'seconds elapsed.')

# Result
# The Unique Phrases are: -  ['0', '01', '011', '0111', '00', '010', '1', '01111']
# The Lempel-Ziv Encoded words are: -  ['00000', '00011', '00101', '00111', '00010', '00100', '00001', '01001']
# 0.00015091896057128906 seconds elapsed.

# When Input Sequence = 000100100000011000010000000100000010100001000000110100010001100
start = time.time()
lempelziv = LempelZivCoding("000100100000011000010000000100000010100001000000110100010001100")
print('The Unique Phrases are: - ', lempelziv.parse_sequence())
print('The Lempel-Ziv Encoded words are: - ',lempelziv.generate_codewords())
end = time.time()
print(end-start, 'seconds elapsed.')

# Result
# The Unique Phrases are: -  ['0', '00', '1', '001', '000', '0001', '10', '00010', '0000', '0010', '00000', '101', '00001', '000000', '11', '01', '000100', '011']
# The Lempel-Ziv Encoded words are: -  ['000000', '000010', '000001', '000101', '000100', '001011', '000110', '001100', '001010', '001000', '010010', '001111', '010011', '010110', '000111', '000011', '010000', '100001']
# 0.0001742839813232422 seconds elapsed.