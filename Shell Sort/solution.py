import time 
import random 

class ShellSort:
    @staticmethod 
    def sort(arr:list, reverse:bool=False) -> list:
        increment = len(arr)//2 
        while increment >= 1:
            for i in range(increment, len(arr)):
                temp = arr[i]
                j = i - increment 
                while j >= 0 and temp<arr[j]:
                    arr[j+increment] = arr[j]
                    j -= increment 

                arr[j+increment] = temp 
            increment //= 2 
        return arr
if __name__ == '__main__':
    s = ShellSort()
    arr1 = random.sample(range(0,1000), 100)
    print(s.sort(arr1))